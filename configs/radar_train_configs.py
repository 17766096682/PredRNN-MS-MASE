# -*- coding: utf-8 -*-
# @Author  : ZhengChang
# @Email   : changzheng18@mails.ucas.ac.cn
import argparse


def configs():
    parser = argparse.ArgumentParser(description='MAU_train')
    parser.add_argument('--data_train_path', type=str, default='../data/')
    parser.add_argument('--data_val_path', type=str, default='../data/')
    parser.add_argument('--data_test_path', type=str, default='../data/')
    parser.add_argument('--pretrained_model', type=str, default='')
    parser.add_argument('--is_training', type=str, default='True')
    parser.add_argument('--device', type=str, default='cuda:0')
    parser.add_argument('--input_length', type=int, default=5)
    parser.add_argument('--real_length', type=int, default=15)
    parser.add_argument('--total_length', type=int, default=15)
    parser.add_argument('--batch_size', type=int, default=8)
    parser.add_argument('--num_workers', type=int, default=2)
    parser.add_argument('--img_height', type=int, default=128)
    parser.add_argument('--img_width', type=int, default=128)
    # parser.add_argument('--sr_size', type=int, default=4)
    parser.add_argument('--img_channel', type=int, default=1)
    parser.add_argument('--patch_size', type=int, default=1)
    parser.add_argument('--model_name', type=str, default='ConvLSTM')
    parser.add_argument('--dataset', type=str, default='radar')
    parser.add_argument('--num_hidden', type=int, default=64)
    parser.add_argument('--num_layers', type=int, default=6)
    parser.add_argument('--filter_size', type=int, default=(3, 3))
    parser.add_argument('--stride', type=int, default=1)
    parser.add_argument('--tau', type=int, default=5)
    parser.add_argument('--layer_norm',type=bool,default=False)
    parser.add_argument('--cell_mode', type=str, default='normal')
    parser.add_argument('--model_mode', type=str, default='normal')
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--lr_decay', type=float, default=0.90)
    parser.add_argument('--delay_interval', type=float, default=2000)
    parser.add_argument('--max_iterations', type=int, default=80000)
    parser.add_argument('--max_epoches', type=int, default=200000)
    # parser.add_argument('--display_interval', type=int, default=1)
    parser.add_argument('--display_interval', type=int, default=10)
    parser.add_argument('--test_interval', type=int, default=5000)
    parser.add_argument('--snapshot_interval', type=int, default=5000)
    parser.add_argument('--num_save_samples', type=int, default=5)
    parser.add_argument('--perforamnce_dir', type=str, default='results/mau/')
    parser.add_argument('--save_dir', type=str, default='checkpoints/mau/')
    parser.add_argument('--gen_frm_dir', type=str, default='results/mau/')
    parser.add_argument('--scheduled_sampling', type=bool, default=True)
    parser.add_argument('--sampling_stop_iter', type=int, default=50000)  #训练到这里的时候开始调整学习率 , 并且取消教学强制策略
    parser.add_argument('--sampling_start_value', type=float, default=1.0)
    parser.add_argument('--sampling_changing_rate', type=float, default=0.00002)
    return parser