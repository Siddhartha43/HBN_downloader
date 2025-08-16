#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EEG檔案自動下載器
從NAS路徑下載指定的EEG檔案到本機資料夾
"""

import os
import shutil
import pandas as pd
from pathlib import Path
import argparse
import logging
from typing import List, Tuple

# 設定日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('eeg_download.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class EEGDownloader:
    def __init__(self, nas_base_path: str = "/mnt/left/home/2025/eegimage/HBN-EEG"):
        """
        初始化下載器
        
        Args:
            nas_base_path: NAS上的基礎路徑
        """
        self.nas_base_path = Path(nas_base_path)
        self.downloaded_count = 0
        self.failed_count = 0
        self.failed_downloads = []
        
    def parse_data_from_text(self, text_content: str) -> List[Tuple[str, str, str]]:
        """
        從文字內容解析資料
        
        Args:
            text_content: 包含ID、回合、任務的文字內容
            
        Returns:
            包含(subject_id, round_num, task_name)的列表
        """
        data = []
        lines = text_content.strip().split('\n')
        
        for line in lines:
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 3:
                    subject_id = parts[0].strip()
                    round_num = parts[1].strip()
                    task_name = parts[2].strip()
                    
                    # 確保回合編號格式正確（移除多餘的R）
                    if round_num.startswith('RR'):
                        round_num = round_num[1:]  # 移除一個R
                    
                    data.append((subject_id, round_num, task_name))
                    
        return data
    
    def parse_data_from_file(self, file_path: str) -> List[Tuple[str, str, str]]:
        """
        從檔案解析資料
        
        Args:
            file_path: 檔案路徑
            
        Returns:
            包含(subject_id, round_num, task_name)的列表
        """
        try:
            # 嘗試讀取為Excel檔案
            if file_path.endswith(('.xlsx', '.xls')):
                df = pd.read_excel(file_path)
                if len(df.columns) >= 3:
                    return list(zip(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2]))
            # 嘗試讀取為CSV/TSV檔案
            elif file_path.endswith(('.csv', '.tsv')):
                sep = '\t' if file_path.endswith('.tsv') else ','
                df = pd.read_csv(file_path, sep=sep)
                if len(df.columns) >= 3:
                    return list(zip(df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2]))
            # 讀取為純文字檔案
            else:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                return self.parse_data_from_text(content)
                
        except Exception as e:
            logger.error(f"讀取檔案失敗: {e}")
            return []
    
    def get_source_file_path(self, subject_id: str, round_num: str, task_name: str) -> Path:
        """
        取得來源檔案路徑
        
        Args:
            subject_id: 受試者ID
            round_num: 回合編號
            task_name: 任務名稱
            
        Returns:
            來源檔案路徑
        """
        # 構建NAS上的檔案路徑
        # 確保回合編號格式正確
        if round_num.startswith('R'):
            round_num = round_num[1:]  # 移除R前綴
        
        round_folder = f"HBN_EEG_R{round_num}"
        subject_folder = subject_id
        eeg_folder = "eeg"
        
        # 處理任務名稱中的run編號
        if '_' in task_name and task_name.split('_')[-1].isdigit():
            # 例如: contrastChangeDetection_1 -> contrastChangeDetection_run-1
            base_task = '_'.join(task_name.split('_')[:-1])
            run_num = task_name.split('_')[-1]
            filename = f"{subject_id}_task-{base_task}_run-{run_num}_eeg.set"
        else:
            # 一般任務名稱
            filename = f"{subject_id}_task-{task_name}_eeg.set"
        
        return self.nas_base_path / round_folder / subject_folder / eeg_folder / filename
    
    def download_file(self, source_path: Path, dest_path: Path) -> bool:
        """
        下載單一檔案
        
        Args:
            source_path: 來源檔案路徑
            dest_path: 目標檔案路徑
            
        Returns:
            下載是否成功
        """
        try:
            if not source_path.exists():
                logger.warning(f"來源檔案不存在: {source_path}")
                return False
                
            # 確保目標目錄存在
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            # 複製檔案
            shutil.copy2(source_path, dest_path)
            logger.info(f"成功下載: {source_path.name}")
            return True
            
        except Exception as e:
            logger.error(f"下載失敗 {source_path}: {e}")
            return False
    
    def download_batch(self, data: List[Tuple[str, str, str]], output_dir: str = "./downloaded_eeg") -> None:
        """
        批次下載檔案
        
        Args:
            data: 包含(subject_id, round_num, task_name)的列表
            output_dir: 輸出目錄
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"開始下載 {len(data)} 個檔案到 {output_path}")
        
        for subject_id, round_num, task_name in data:
            source_path = self.get_source_file_path(subject_id, round_num, task_name)
            # 確保回合編號格式正確用於檔案命名
            clean_round = round_num
            if clean_round.startswith('R'):
                clean_round = clean_round[1:]  # 移除R前綴
            dest_path = output_path / f"{subject_id}_R{clean_round}_{task_name}.set"
            
            if self.download_file(source_path, dest_path):
                self.downloaded_count += 1
            else:
                self.failed_count += 1
                self.failed_downloads.append((subject_id, round_num, task_name))
        
        # 輸出統計資訊
        logger.info(f"下載完成! 成功: {self.downloaded_count}, 失敗: {self.failed_count}")
        
        if self.failed_downloads:
            logger.info("失敗的下載:")
            for subject_id, round_num, task_name in self.failed_downloads:
                logger.info(f"  {subject_id} R{round_num} {task_name}")

def main():
    parser = argparse.ArgumentParser(description='EEG檔案自動下載器')
    parser.add_argument('--input', '-i', help='輸入檔案路徑 (Excel, CSV, TSV 或文字檔案)')
    parser.add_argument('--text', '-t', help='直接輸入文字內容')
    parser.add_argument('--output', '-o', default='./downloaded_eeg', help='輸出目錄')
    parser.add_argument('--nas-path', default='/mnt/left/home/2025/eegimage/HBN-EEG', help='NAS基礎路徑')
    
    args = parser.parse_args()
    
    downloader = EEGDownloader(args.nas_path)
    
    if args.input:
        # 從檔案讀取資料
        data = downloader.parse_data_from_file(args.input)
    elif args.text:
        # 從文字內容讀取資料
        data = downloader.parse_data_from_text(args.text)
    else:
        # 使用範例資料
        example_text = """sub-NDARAU044FP6	R10	ThePresent
sub-NDARCA851LUG	R10	DiaryOfAWimpyKid
sub-NDARGD414MUA	R10	DiaryOfAWimpyKid"""
        data = downloader.parse_data_from_text(example_text)
        logger.info("使用範例資料進行測試")
    
    if data:
        downloader.download_batch(data, args.output)
    else:
        logger.error("沒有找到有效的資料")

if __name__ == "__main__":
    main()
