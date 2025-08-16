#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡化的EEG檔案下載器
直接使用您提供的資料進行下載
"""

from eeg_downloader import EEGDownloader

def main():
    # 您提供的資料
    data_text = """sub-NDARAU044FP6	R10	ThePresent
sub-NDARCA851LUG	R10	DiaryOfAWimpyKid
sub-NDARGD414MUA	R10	DiaryOfAWimpyKid
sub-NDARGK981YLX	R10	DiaryOfAWimpyKid
sub-NDARPL898TYW	R10	DiaryOfAWimpyKid
sub-NDARTH261GB5	R10	DiaryOfAWimpyKid
sub-NDARAR935TGZ	R10	symbolSearch
sub-NDARVB588TM7	R10	contrastChangeDetection_1
sub-NDARDP740CLE	R10	contrastChangeDetection_2
sub-NDARXJ635PWG	R10	contrastChangeDetection_3
sub-NDARUZ062BWR	R10	surroundSupp_1
sub-NDARHR621FJB	R10	surroundSupp_2
sub-NDARUX422KT3	R11	RestingState
sub-NDARDV550JB2	R11	RestingState
sub-NDARAU517MC6	R11	RestingState
sub-NDARWT403LP6	R11	DespicableMe
sub-NDARHN206XY3	R11	DespicableMe
sub-NDARGJ317VC9	R11	DespicableMe
sub-NDARFX158KKM	R11	FunwithFractals
sub-NDARDW550GU6	R11	FunwithFractals
sub-NDARWG174EZD	R11	FunwithFractals
sub-NDARCZ465CMY	R11	ThePresent
sub-NDARVA602LMV	R11	ThePresent
sub-NDARXE058PZF	R11	ThePresent
sub-NDARRE588NRM	R11	DiaryOfAWimpyKid
sub-NDARCH755TLW	R11	DiaryOfAWimpyKid
sub-NDARRX900GP4	R11	DiaryOfAWimpyKid
sub-NDARNN321YCR	R11	symbolSearch
sub-NDARAU517MC6	R11	symbolSearch
sub-NDARBE096YK6	R11	contrastChangeDetection_1
sub-NDARDV550JB2	R11	contrastChangeDetection_1
sub-NDARKW511VE6	R11	contrastChangeDetection_2
sub-NDARLK158UN6	R11	contrastChangeDetection_2
sub-NDARMH305FWL	R11	contrastChangeDetection_3
sub-NDARPP238VMX	R11	contrastChangeDetection_3
sub-NDARAW620GJ8	R11	surroundSupp_1
sub-NDARVM326HYM	R11	surroundSupp_1
sub-NDARJJ856NTT	R11	surroundSupp_2
sub-NDARYH501UH3	R11	surroundSupp_2"""

    # 初始化下載器
    downloader = EEGDownloader()
    
    # 解析資料
    data = downloader.parse_data_from_text(data_text)
    
    # 開始下載
    print(f"準備下載 {len(data)} 個檔案...")
    downloader.download_batch(data, "./my_eeg_files")
    
    print("下載完成!")

if __name__ == "__main__":
    main()
