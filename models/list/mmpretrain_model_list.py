mmpretrain_model_list = [
    'barlowtwins_resnet50_8xb256-coslr-300e_in1k', 'beit-base-p16_beit-in21k-pre_3rdparty_in1k',
    'beit-base-p16_beit-pre_8xb128-coslr-100e_in1k',
    'beit-base-p16_beitv2-in21k-pre_3rdparty_in1k',
    'beit-base-p16_beitv2-pre_8xb128-coslr-100e_in1k',
    'beit-base-p16_cae-pre_8xb128-coslr-100e_in1k', 'beit-g-p14_3rdparty-eva_30m',
    'beit-g-p14_eva-30m-in21k-pre_3rdparty_in1k-336px',
    'beit-g-p14_eva-30m-in21k-pre_3rdparty_in1k-560px', 'beit-g-p14_eva-30m-pre_3rdparty_in21k',
    'beit-g-p16_3rdparty-eva_30m', 'beit-l-p14_3rdparty-eva_in21k',
    'beit-l-p14_eva-in21k-pre_3rdparty_in1k-196px', 'beit-l-p14_eva-in21k-pre_3rdparty_in1k-336px',
    'beit-l-p14_eva-pre_3rdparty_in1k-196px', 'beit-l-p14_eva-pre_3rdparty_in1k-336px',
    'beit-l-p14_eva-pre_3rdparty_in21k', 'beit_beit-base-p16_8xb256-amp-coslr-300e_in1k',
    'beitv2_beit-base-p16_8xb256-amp-coslr-300e_in1k', 'blip-base_3rdparty_caption',
    'blip-base_3rdparty_nlvr', 'blip-base_3rdparty_retrieval', 'blip-base_3rdparty_vqa',
    'blip-base_8xb16_refcoco', 'blip2-opt2.7b_3rdparty-zeroshot_caption',
    'blip2-opt2.7b_3rdparty-zeroshot_vqa', 'blip2_3rdparty_retrieval',
    'byol_resnet50_16xb256-coslr-200e_in1k', 'cae_beit-base-p16_8xb256-amp-coslr-300e_in1k',
    'cn-clip_resnet50_zeroshot-cls_cifar100', 'cn-clip_vit-base-p16_zeroshot-cls_cifar100',
    'cn-clip_vit-huge-p14_zeroshot-cls_cifar100', 'cn-clip_vit-large-p14_zeroshot-cls_cifar100',
    'conformer-base-p16_3rdparty_in1k', 'conformer-small-p16_3rdparty_in1k',
    'conformer-small-p32_8xb128_in1k', 'conformer-tiny-p16_3rdparty_in1k',
    'convmixer-1024-20_3rdparty_in1k', 'convmixer-1536-20_3rdparty_in1k',
    'convmixer-768-32_3rdparty_in1k', 'convnext-base_32xb128-noema_in1k',
    'convnext-base_32xb128_in1k', 'convnext-base_3rdparty-noema_in1k',
    'convnext-base_3rdparty_in1k', 'convnext-base_3rdparty_in1k-384px',
    'convnext-base_3rdparty_in21k', 'convnext-base_in21k-pre-3rdparty_in1k-384px',
    'convnext-base_in21k-pre_3rdparty_in1k', 'convnext-large_3rdparty_in1k',
    'convnext-large_3rdparty_in1k-384px', 'convnext-large_3rdparty_in21k',
    'convnext-large_in21k-pre-3rdparty_in1k-384px', 'convnext-large_in21k-pre_3rdparty_in1k',
    'convnext-small_32xb128-noema_in1k', 'convnext-small_32xb128_in1k',
    'convnext-small_in21k-pre_3rdparty_in1k', 'convnext-small_in21k-pre_3rdparty_in1k-384px',
    'convnext-tiny_32xb128-noema_in1k', 'convnext-tiny_32xb128_in1k',
    'convnext-tiny_in21k-pre_3rdparty_in1k', 'convnext-tiny_in21k-pre_3rdparty_in1k-384px',
    'convnext-v2-atto_3rdparty-fcmae_in1k', 'convnext-v2-atto_fcmae-pre_3rdparty_in1k',
    'convnext-v2-base_3rdparty-fcmae_in1k', 'convnext-v2-base_fcmae-in21k-pre_3rdparty_in1k',
    'convnext-v2-base_fcmae-in21k-pre_3rdparty_in1k-384px',
    'convnext-v2-base_fcmae-pre_3rdparty_in1k', 'convnext-v2-femto_3rdparty-fcmae_in1k',
    'convnext-v2-femto_fcmae-pre_3rdparty_in1k', 'convnext-v2-huge_3rdparty-fcmae_in1k',
    'convnext-v2-huge_fcmae-in21k-pre_3rdparty_in1k-384px',
    'convnext-v2-huge_fcmae-in21k-pre_3rdparty_in1k-512px',
    'convnext-v2-huge_fcmae-pre_3rdparty_in1k', 'convnext-v2-large_3rdparty-fcmae_in1k',
    'convnext-v2-large_fcmae-in21k-pre_3rdparty_in1k',
    'convnext-v2-large_fcmae-in21k-pre_3rdparty_in1k-384px',
    'convnext-v2-large_fcmae-pre_3rdparty_in1k', 'convnext-v2-nano_3rdparty-fcmae_in1k',
    'convnext-v2-nano_fcmae-in21k-pre_3rdparty_in1k',
    'convnext-v2-nano_fcmae-in21k-pre_3rdparty_in1k-384px',
    'convnext-v2-nano_fcmae-pre_3rdparty_in1k', 'convnext-v2-pico_3rdparty-fcmae_in1k',
    'convnext-v2-pico_fcmae-pre_3rdparty_in1k', 'convnext-v2-tiny_3rdparty-fcmae_in1k',
    'convnext-v2-tiny_fcmae-in21k-pre_3rdparty_in1k',
    'convnext-v2-tiny_fcmae-in21k-pre_3rdparty_in1k-384px',
    'convnext-v2-tiny_fcmae-pre_3rdparty_in1k', 'convnext-xlarge_3rdparty_in21k',
    'convnext-xlarge_in21k-pre-3rdparty_in1k-384px', 'convnext-xlarge_in21k-pre_3rdparty_in1k',
    'convnextv2-tiny_spark-pre_300e_in1k', 'cspdarknet50_3rdparty_8xb32_in1k',
    'cspresnet50_3rdparty_8xb32_in1k', 'cspresnext50_3rdparty_8xb32_in1k',
    'davit-base_3rdparty_in1k', 'davit-small_3rdparty_in1k', 'davit-tiny_3rdparty_in1k',
    'deit-base-distilled_224px-pre_3rdparty_in1k-384px', 'deit-base-distilled_3rdparty_in1k',
    'deit-base_16xb64_in1k', 'deit-base_224px-pre_3rdparty_in1k-384px', 'deit-base_3rdparty_in1k',
    'deit-small-distilled_3rdparty_in1k', 'deit-small_4xb256_in1k',
    'deit-tiny-distilled_3rdparty_in1k', 'deit-tiny_4xb256_in1k', 'deit3-base-p16_3rdparty_in1k',
    'deit3-base-p16_3rdparty_in1k-384px', 'deit3-base-p16_in21k-pre_3rdparty_in1k',
    'deit3-base-p16_in21k-pre_3rdparty_in1k-384px', 'deit3-huge-p14_3rdparty_in1k',
    'deit3-huge-p14_in21k-pre_3rdparty_in1k', 'deit3-large-p16_3rdparty_in1k',
    'deit3-large-p16_3rdparty_in1k-384px', 'deit3-large-p16_in21k-pre_3rdparty_in1k',
    'deit3-large-p16_in21k-pre_3rdparty_in1k-384px', 'deit3-medium-p16_3rdparty_in1k',
    'deit3-medium-p16_in21k-pre_3rdparty_in1k', 'deit3-small-p16_3rdparty_in1k',
    'deit3-small-p16_3rdparty_in1k-384px', 'deit3-small-p16_in21k-pre_3rdparty_in1k',
    'deit3-small-p16_in21k-pre_3rdparty_in1k-384px', 'densecl_resnet50_8xb32-coslr-200e_in1k',
    'densenet121_3rdparty_in1k', 'densenet161_3rdparty_in1k', 'densenet169_3rdparty_in1k',
    'densenet201_3rdparty_in1k', 'edgenext-base_3rdparty-usi_in1k', 'edgenext-base_3rdparty_in1k',
    'edgenext-small-usi_3rdparty_in1k', 'edgenext-small_3rdparty_in1k',
    'edgenext-xsmall_3rdparty_in1k', 'edgenext-xxsmall_3rdparty_in1k',
    'efficientformer-l1_3rdparty_8xb128_in1k', 'efficientformer-l3_3rdparty_8xb128_in1k',
    'efficientformer-l7_3rdparty_8xb128_in1k', 'efficientnet-b0_3rdparty-ra-noisystudent_in1k',
    'efficientnet-b0_3rdparty_8xb32-aa-advprop_in1k', 'efficientnet-b0_3rdparty_8xb32-aa_in1k',
    'efficientnet-b0_3rdparty_8xb32_in1k', 'efficientnet-b1_3rdparty-ra-noisystudent_in1k',
    'efficientnet-b1_3rdparty_8xb32-aa-advprop_in1k', 'efficientnet-b1_3rdparty_8xb32-aa_in1k',
    'efficientnet-b1_3rdparty_8xb32_in1k', 'efficientnet-b2_3rdparty-ra-noisystudent_in1k',
    'efficientnet-b2_3rdparty_8xb32-aa-advprop_in1k', 'efficientnet-b2_3rdparty_8xb32-aa_in1k',
    'efficientnet-b2_3rdparty_8xb32_in1k', 'efficientnet-b3_3rdparty-ra-noisystudent_in1k',
    'efficientnet-b3_3rdparty_8xb32-aa-advprop_in1k', 'efficientnet-b3_3rdparty_8xb32-aa_in1k',
    'efficientnet-b3_3rdparty_8xb32_in1k', 'efficientnet-b4_3rdparty-ra-noisystudent_in1k',
    'efficientnet-b4_3rdparty_8xb32-aa-advprop_in1k', 'efficientnet-b4_3rdparty_8xb32-aa_in1k',
    'efficientnet-b4_3rdparty_8xb32_in1k', 'efficientnet-b5_3rdparty-ra-noisystudent_in1k',
    'efficientnet-b5_3rdparty_8xb32-aa-advprop_in1k', 'efficientnet-b5_3rdparty_8xb32-aa_in1k',
    'efficientnet-b5_3rdparty_8xb32_in1k', 'efficientnet-b6_3rdparty-ra-noisystudent_in1k',
    'efficientnet-b6_3rdparty_8xb32-aa-advprop_in1k', 'efficientnet-b6_3rdparty_8xb32-aa_in1k',
    'efficientnet-b7_3rdparty-ra-noisystudent_in1k',
    'efficientnet-b7_3rdparty_8xb32-aa-advprop_in1k', 'efficientnet-b7_3rdparty_8xb32-aa_in1k',
    'efficientnet-b8_3rdparty_8xb32-aa-advprop_in1k',
    'efficientnet-l2_3rdparty-ra-noisystudent_in1k-475px',
    'efficientnet-l2_3rdparty-ra-noisystudent_in1k-800px', 'efficientnetv2-b0_3rdparty_in1k',
    'efficientnetv2-b1_3rdparty_in1k', 'efficientnetv2-b2_3rdparty_in1k',
    'efficientnetv2-b3_3rdparty_in1k', 'efficientnetv2-l_3rdparty_in1k',
    'efficientnetv2-l_3rdparty_in21k', 'efficientnetv2-l_in21k-pre_3rdparty_in1k',
    'efficientnetv2-m_3rdparty_in1k', 'efficientnetv2-m_3rdparty_in21k',
    'efficientnetv2-m_in21k-pre_3rdparty_in1k', 'efficientnetv2-s_3rdparty_in1k',
    'efficientnetv2-s_3rdparty_in21k', 'efficientnetv2-s_in21k-pre_3rdparty_in1k',
    'efficientnetv2-xl_3rdparty_in21k', 'efficientnetv2-xl_in21k-pre_3rdparty_in1k',
    'eva-mae-style_vit-base-p16_16xb256-coslr-400e_in1k', 'flamingo_3rdparty-zeroshot_caption',
    'flamingo_3rdparty-zeroshot_vqa', 'hivit-base-p16_16xb64_in1k', 'hivit-small-p16_16xb64_in1k',
    'hivit-tiny-p16_16xb64_in1k', 'hornet-base-gf_3rdparty_in1k', 'hornet-base_3rdparty_in1k',
    'hornet-small-gf_3rdparty_in1k', 'hornet-small_3rdparty_in1k', 'hornet-tiny-gf_3rdparty_in1k',
    'hornet-tiny_3rdparty_in1k', 'hrnet-w18_3rdparty_8xb32-ssld_in1k',
    'hrnet-w18_3rdparty_8xb32_in1k', 'hrnet-w30_3rdparty_8xb32_in1k',
    'hrnet-w32_3rdparty_8xb32_in1k', 'hrnet-w40_3rdparty_8xb32_in1k',
    'hrnet-w44_3rdparty_8xb32_in1k', 'hrnet-w48_3rdparty_8xb32-ssld_in1k',
    'hrnet-w48_3rdparty_8xb32_in1k', 'hrnet-w64_3rdparty_8xb32_in1k',
    'inception-v3_3rdparty_8xb32_in1k', 'itpn-clip-b_hivit-base-p16_8xb256-amp-coslr-800e_in1k',
    'itpn-pixel_hivit-base-p16_8xb512-amp-coslr-800e_in1k',
    'itpn-pixel_hivit-large-p16_8xb512-amp-coslr-800e_in1k', 'levit-128_3rdparty_in1k',
    'levit-128s_3rdparty_in1k', 'levit-192_3rdparty_in1k', 'levit-256_3rdparty_in1k',
    'levit-384_3rdparty_in1k', 'llava-7b-v1_caption',
    'mae_vit-base-p16_8xb512-amp-coslr-1600e_in1k', 'mae_vit-base-p16_8xb512-amp-coslr-300e_in1k',
    'mae_vit-base-p16_8xb512-amp-coslr-400e_in1k', 'mae_vit-base-p16_8xb512-amp-coslr-800e_in1k',
    'mae_vit-huge-p16_8xb512-amp-coslr-1600e_in1k',
    'mae_vit-large-p16_8xb512-amp-coslr-1600e_in1k',
    'mae_vit-large-p16_8xb512-amp-coslr-400e_in1k', 'mae_vit-large-p16_8xb512-amp-coslr-800e_in1k',
    'maskfeat_vit-base-p16_8xb256-amp-coslr-300e_in1k',
    'mff_vit-base-p16_8xb512-amp-coslr-300e_in1k', 'mff_vit-base-p16_8xb512-amp-coslr-800e_in1k',
    'milan_vit-base-p16_16xb256-amp-coslr-400e_in1k', 'minigpt-4_vicuna-7b_caption',
    'mixmim-base_mixmim-pre_8xb128-coslr-100e_in1k', 'mixmim_mixmim-base_16xb128-coslr-300e_in1k',
    'mlp-mixer-base-p16_3rdparty_64xb64_in1k', 'mlp-mixer-large-p16_3rdparty_64xb64_in1k',
    'mobilenet-v2_8xb32_in1k', 'mobilenet-v3-large_3rdparty_in1k',
    'mobilenet-v3-large_8xb128_in1k', 'mobilenet-v3-small-050_3rdparty_in1k',
    'mobilenet-v3-small-075_3rdparty_in1k', 'mobilenet-v3-small_3rdparty_in1k',
    'mobilenet-v3-small_8xb128_in1k', 'mobileone-s0_8xb32_in1k', 'mobileone-s1_8xb32_in1k',
    'mobileone-s2_8xb32_in1k', 'mobileone-s3_8xb32_in1k', 'mobileone-s4_8xb32_in1k',
    'mobilevit-small_3rdparty_in1k', 'mobilevit-xsmall_3rdparty_in1k',
    'mobilevit-xxsmall_3rdparty_in1k', 'mocov2_resnet50_8xb32-coslr-200e_in1k',
    'mocov3_resnet50_8xb512-amp-coslr-100e_in1k', 'mocov3_resnet50_8xb512-amp-coslr-300e_in1k',
    'mocov3_resnet50_8xb512-amp-coslr-800e_in1k',
    'mocov3_vit-base-p16_16xb256-amp-coslr-300e_in1k',
    'mocov3_vit-large-p16_64xb64-amp-coslr-300e_in1k',
    'mocov3_vit-small-p16_16xb256-amp-coslr-300e_in1k', 'mvitv2-base_3rdparty_in1k',
    'mvitv2-large_3rdparty_in1k', 'mvitv2-small_3rdparty_in1k', 'mvitv2-tiny_3rdparty_in1k',
    'ofa-base_3rdparty-finetuned_caption', 'ofa-base_3rdparty-finetuned_refcoco',
    'ofa-base_3rdparty-finetuned_vqa', 'ofa-base_3rdparty-zeroshot_vqa',
    'otter-9b_3rdparty_caption', 'otter-9b_3rdparty_vqa', 'poolformer-m36_3rdparty_32xb128_in1k',
    'poolformer-m48_3rdparty_32xb128_in1k', 'poolformer-s12_3rdparty_32xb128_in1k',
    'poolformer-s24_3rdparty_32xb128_in1k', 'poolformer-s36_3rdparty_32xb128_in1k',
    'pvig-base_3rdparty_in1k', 'pvig-medium_3rdparty_in1k', 'pvig-small_3rdparty_in1k',
    'pvig-tiny_3rdparty_in1k', 'regnetx-1.6gf_8xb128_in1k', 'regnetx-12gf_8xb64_in1k',
    'regnetx-3.2gf_8xb64_in1k', 'regnetx-4.0gf_8xb64_in1k', 'regnetx-400mf_8xb128_in1k',
    'regnetx-6.4gf_8xb64_in1k', 'regnetx-8.0gf_8xb64_in1k', 'regnetx-800mf_8xb128_in1k',
    'replknet-31b_3rdparty_in1k', 'replknet-31b_3rdparty_in1k-384px',
    'replknet-31b_in21k-pre_3rdparty_in1k', 'replknet-31b_in21k-pre_3rdparty_in1k-384px',
    'replknet-31l_in21k-pre_3rdparty_in1k-384px', 'replknet-xl_meg73m-pre_3rdparty_in1k-320px',
    'repmlp-base_3rdparty_8xb64_in1k', 'repmlp-base_3rdparty_8xb64_in1k-256px',
    'repvgg-a0_8xb32_in1k', 'repvgg-a1_8xb32_in1k', 'repvgg-a2_8xb32_in1k', 'repvgg-b0_8xb32_in1k',
    'repvgg-b1_8xb32_in1k', 'repvgg-b1g2_8xb32_in1k', 'repvgg-b1g4_8xb32_in1k',
    'repvgg-b2_8xb32_in1k', 'repvgg-b2g4_8xb32_in1k', 'repvgg-b3_8xb32_in1k',
    'repvgg-b3g4_8xb32_in1k', 'repvgg-d2se_3rdparty_in1k', 'res2net101-w26-s4_3rdparty_8xb32_in1k',
    'res2net50-w14-s8_3rdparty_8xb32_in1k', 'res2net50-w26-s8_3rdparty_8xb32_in1k',
    'resnet101-csra_1xb16_voc07-448px', 'resnet101_8xb16_cifar10', 'resnet101_8xb32_in1k',
    'resnet152_8xb16_cifar10', 'resnet152_8xb32_in1k', 'resnet18_8xb16_cifar10',
    'resnet18_8xb32_in1k', 'resnet34_8xb16_cifar10', 'resnet34_8xb32_in1k',
    'resnet50-arcface_inshop', 'resnet50_8xb16_cifar10', 'resnet50_8xb16_cifar100',
    'resnet50_8xb256-rsb-a1-600e_in1k', 'resnet50_8xb256-rsb-a2-300e_in1k',
    'resnet50_8xb256-rsb-a3-100e_in1k', 'resnet50_8xb32-fp16_in1k', 'resnet50_8xb32_in1k',
    'resnet50_8xb8_cub', 'resnet50_barlowtwins-pre_8xb32-linear-coslr-100e_in1k',
    'resnet50_byol-pre_8xb512-linear-coslr-90e_in1k',
    'resnet50_densecl-pre_8xb32-linear-steplr-100e_in1k',
    'resnet50_mocov2-pre_8xb32-linear-steplr-100e_in1k',
    'resnet50_mocov3-100e-pre_8xb128-linear-coslr-90e_in1k',
    'resnet50_mocov3-300e-pre_8xb128-linear-coslr-90e_in1k',
    'resnet50_mocov3-800e-pre_8xb128-linear-coslr-90e_in1k',
    'resnet50_simclr-200e-pre_8xb512-linear-coslr-90e_in1k',
    'resnet50_simclr-800e-pre_8xb512-linear-coslr-90e_in1k',
    'resnet50_simsiam-100e-pre_8xb512-linear-coslr-90e_in1k',
    'resnet50_simsiam-200e-pre_8xb512-linear-coslr-90e_in1k', 'resnet50_spark-pre_300e_in1k',
    'resnet50_swav-pre_8xb32-linear-coslr-100e_in1k', 'resnetv1c101_8xb32_in1k',
    'resnetv1c152_8xb32_in1k', 'resnetv1c50_8xb32_in1k', 'resnetv1d101_8xb32_in1k',
    'resnetv1d152_8xb32_in1k', 'resnetv1d50_8xb32_in1k', 'resnext101-32x4d_8xb32_in1k',
    'resnext101-32x8d_8xb32_in1k', 'resnext152-32x4d_8xb32_in1k', 'resnext50-32x4d_8xb32_in1k',
    'revvit-base_3rdparty_in1k', 'revvit-small_3rdparty_in1k', 'riformer-m36_in1k',
    'riformer-m36_in1k-384', 'riformer-m48_in1k', 'riformer-m48_in1k-384', 'riformer-s12_in1k',
    'riformer-s12_in1k-384', 'riformer-s24_in1k', 'riformer-s24_in1k-384', 'riformer-s36_in1k',
    'riformer-s36_in1k-384', 'seresnet101_8xb32_in1k', 'seresnet50_8xb32_in1k',
    'shufflenet-v1-1x_16xb64_in1k', 'shufflenet-v2-1x_16xb64_in1k',
    'simclr_resnet50_16xb256-coslr-200e_in1k', 'simclr_resnet50_16xb256-coslr-800e_in1k',
    'simmim_swin-base-w6_16xb128-amp-coslr-800e_in1k-192px',
    'simmim_swin-base-w6_8xb256-amp-coslr-100e_in1k-192px',
    'simmim_swin-large-w12_16xb128-amp-coslr-800e_in1k-192px',
    'simsiam_resnet50_8xb32-coslr-100e_in1k', 'simsiam_resnet50_8xb32-coslr-200e_in1k',
    'spark_sparse-convnextv2-tiny_800e_in1k', 'spark_sparse-resnet50_800e_in1k',
    'swav_resnet50_8xb32-mcrop-coslr-200e_in1k-224px-96px',
    'swin-base-w6_simmim-100e-pre_8xb256-coslr-100e_in1k-192px',
    'swin-base-w6_simmim-800e-pre_8xb256-coslr-100e_in1k-192px',
    'swin-base-w7_simmim-100e-pre_8xb256-coslr-100e_in1k', 'swin-base_16xb64_in1k',
    'swin-base_3rdparty_in1k', 'swin-base_3rdparty_in1k-384', 'swin-base_in21k-pre-3rdparty_in1k',
    'swin-base_in21k-pre-3rdparty_in1k-384', 'swin-l_glip-pre_3rdparty_384px',
    'swin-large-w14_simmim-800e-pre_8xb256-coslr-100e_in1k', 'swin-large_8xb8_cub-384px',
    'swin-large_in21k-pre-3rdparty_in1k', 'swin-large_in21k-pre-3rdparty_in1k-384',
    'swin-small_16xb64_in1k', 'swin-small_3rdparty_in1k', 'swin-t_glip-pre_3rdparty',
    'swin-tiny_16xb64_in1k', 'swin-tiny_3rdparty_in1k', 'swinv2-base-w12_3rdparty_in21k-192px',
    'swinv2-base-w16_3rdparty_in1k-256px', 'swinv2-base-w16_in21k-pre_3rdparty_in1k-256px',
    'swinv2-base-w24_in21k-pre_3rdparty_in1k-384px', 'swinv2-base-w8_3rdparty_in1k-256px',
    'swinv2-large-w12_3rdparty_in21k-192px', 'swinv2-large-w16_in21k-pre_3rdparty_in1k-256px',
    'swinv2-large-w24_in21k-pre_3rdparty_in1k-384px', 'swinv2-small-w16_3rdparty_in1k-256px',
    'swinv2-small-w8_3rdparty_in1k-256px', 'swinv2-tiny-w16_3rdparty_in1k-256px',
    'swinv2-tiny-w8_3rdparty_in1k-256px', 't2t-vit-t-14_8xb64_in1k', 't2t-vit-t-19_8xb64_in1k',
    't2t-vit-t-24_8xb64_in1k', 'tinyvit-11m_3rdparty_in1k',
    'tinyvit-11m_in21k-distill-pre_3rdparty_in1k', 'tinyvit-21m_3rdparty_in1k',
    'tinyvit-21m_in21k-distill-pre_3rdparty_in1k',
    'tinyvit-21m_in21k-distill-pre_3rdparty_in1k-384px',
    'tinyvit-21m_in21k-distill-pre_3rdparty_in1k-512px', 'tinyvit-5m_3rdparty_in1k',
    'tinyvit-5m_in21k-distill-pre_3rdparty_in1k', 'tnt-small-p16_3rdparty_in1k',
    'twins-pcpvt-base_3rdparty_8xb128_in1k', 'twins-pcpvt-large_3rdparty_16xb64_in1k',
    'twins-pcpvt-small_3rdparty_8xb128_in1k', 'twins-svt-base_8xb128_3rdparty_in1k',
    'twins-svt-large_3rdparty_16xb64_in1k', 'twins-svt-small_3rdparty_8xb128_in1k',
    'van-base_3rdparty_in1k', 'van-large_3rdparty_in1k', 'van-small_3rdparty_in1k',
    'van-tiny_3rdparty_in1k', 'vgg11_8xb32_in1k', 'vgg11bn_8xb32_in1k', 'vgg13_8xb32_in1k',
    'vgg13bn_8xb32_in1k', 'vgg16_8xb32_in1k', 'vgg16bn_8xb32_in1k', 'vgg19_8xb32_in1k',
    'vgg19bn_8xb32_in1k', 'vig-base_3rdparty_in1k', 'vig-small_3rdparty_in1k',
    'vig-tiny_3rdparty_in1k', 'vit-base-p14_dinov2-pre_3rdparty',
    'vit-base-p14_eva02-in21k-pre_3rdparty_in1k-448px',
    'vit-base-p14_eva02-in21k-pre_in21k-medft_3rdparty_in1k-448px', 'vit-base-p14_eva02-pre_in21k',
    'vit-base-p16_32xb128-mae_in1k', 'vit-base-p16_clip-laion2b-in12k-pre_3rdparty_in1k',
    'vit-base-p16_clip-laion2b-in12k-pre_3rdparty_in1k-384px',
    'vit-base-p16_clip-laion2b-pre_3rdparty_in1k',
    'vit-base-p16_clip-laion2b-pre_3rdparty_in1k-384px',
    'vit-base-p16_clip-openai-in12k-pre_3rdparty_in1k',
    'vit-base-p16_clip-openai-in12k-pre_3rdparty_in1k-384px',
    'vit-base-p16_clip-openai-pre_3rdparty_in1k',
    'vit-base-p16_clip-openai-pre_3rdparty_in1k-384px',
    'vit-base-p16_eva-mae-style-pre_8xb128-coslr-100e_in1k',
    'vit-base-p16_eva-mae-style-pre_8xb2048-linear-coslr-100e_in1k',
    'vit-base-p16_in21k-pre_3rdparty_in1k-384px',
    'vit-base-p16_mae-1600e-pre_8xb128-coslr-100e_in1k',
    'vit-base-p16_mae-1600e-pre_8xb2048-linear-coslr-90e_in1k',
    'vit-base-p16_mae-300e-pre_8xb128-coslr-100e_in1k',
    'vit-base-p16_mae-300e-pre_8xb2048-linear-coslr-90e_in1k',
    'vit-base-p16_mae-400e-pre_8xb128-coslr-100e_in1k',
    'vit-base-p16_mae-400e-pre_8xb2048-linear-coslr-90e_in1k',
    'vit-base-p16_mae-800e-pre_8xb128-coslr-100e_in1k',
    'vit-base-p16_mae-800e-pre_8xb2048-linear-coslr-90e_in1k',
    'vit-base-p16_maskfeat-pre_8xb256-coslr-100e_in1k',
    'vit-base-p16_mff-300e-pre_8xb128-coslr-100e_in1k',
    'vit-base-p16_mff-300e-pre_8xb2048-linear-coslr-90e_in1k',
    'vit-base-p16_mff-800e-pre_8xb128-coslr-100e_in1k',
    'vit-base-p16_mff-800e-pre_8xb2048-linear-coslr-90e_in1k',
    'vit-base-p16_milan-pre_8xb128-coslr-100e_in1k',
    'vit-base-p16_milan-pre_8xb2048-linear-coslr-100e_in1k',
    'vit-base-p16_mocov3-pre_8xb128-linear-coslr-90e_in1k',
    'vit-base-p16_mocov3-pre_8xb64-coslr-150e_in1k', 'vit-base-p16_sam-pre_3rdparty_sa1b-1024px',
    'vit-base-p32_clip-laion2b-in12k-pre_3rdparty_in1k',
    'vit-base-p32_clip-laion2b-in12k-pre_3rdparty_in1k-384px',
    'vit-base-p32_clip-laion2b-in12k-pre_3rdparty_in1k-448px',
    'vit-base-p32_clip-laion2b-pre_3rdparty_in1k',
    'vit-base-p32_clip-openai-in12k-pre_3rdparty_in1k-384px',
    'vit-base-p32_clip-openai-pre_3rdparty_in1k', 'vit-base-p32_in21k-pre_3rdparty_in1k-384px',
    'vit-giant-p14_dinov2-pre_3rdparty', 'vit-huge-p14_mae-1600e-pre_32xb8-coslr-50e_in1k-448px',
    'vit-huge-p14_mae-1600e-pre_8xb128-coslr-50e_in1k',
    'vit-huge-p16_sam-pre_3rdparty_sa1b-1024px', 'vit-large-p14_clip-openai-pre_3rdparty',
    'vit-large-p14_dinov2-pre_3rdparty',
    'vit-large-p14_eva02-in21k-pre_in21k-medft_3rdparty_in1k-448px',
    'vit-large-p14_eva02-pre_in21k', 'vit-large-p14_eva02-pre_m38m',
    'vit-large-p14_eva02_m38m-pre_in21k-medft_3rdparty_in1k-448px',
    'vit-large-p16_in21k-pre_3rdparty_in1k-384px',
    'vit-large-p16_mae-1600e-pre_8xb128-coslr-50e_in1k',
    'vit-large-p16_mae-1600e-pre_8xb2048-linear-coslr-90e_in1k',
    'vit-large-p16_mae-400e-pre_8xb128-coslr-50e_in1k',
    'vit-large-p16_mae-400e-pre_8xb2048-linear-coslr-90e_in1k',
    'vit-large-p16_mae-800e-pre_8xb128-coslr-50e_in1k',
    'vit-large-p16_mae-800e-pre_8xb2048-linear-coslr-90e_in1k',
    'vit-large-p16_mocov3-pre_8xb64-coslr-100e_in1k', 'vit-large-p16_sam-pre_3rdparty_sa1b-1024px',
    'vit-small-p14_dinov2-pre_3rdparty', 'vit-small-p14_eva02-in21k-pre_3rdparty_in1k-336px',
    'vit-small-p14_eva02-pre_in21k', 'vit-small-p16_mocov3-pre_8xb128-linear-coslr-90e_in1k',
    'vit-tiny-p14_eva02-in21k-pre_3rdparty_in1k-336px', 'vit-tiny-p14_eva02-pre_in21k',
    'wide-resnet101_3rdparty_8xb32_in1k', 'wide-resnet50_3rdparty-timm_8xb32_in1k',
    'wide-resnet50_3rdparty_8xb32_in1k', 'xcit-large-24-p16_3rdparty-dist_in1k',
    'xcit-large-24-p16_3rdparty-dist_in1k-384px', 'xcit-large-24-p16_3rdparty_in1k',
    'xcit-large-24-p8_3rdparty-dist_in1k', 'xcit-large-24-p8_3rdparty-dist_in1k-384px',
    'xcit-large-24-p8_3rdparty_in1k', 'xcit-medium-24-p16_3rdparty-dist_in1k',
    'xcit-medium-24-p16_3rdparty-dist_in1k-384px', 'xcit-medium-24-p16_3rdparty_in1k',
    'xcit-medium-24-p8_3rdparty-dist_in1k', 'xcit-medium-24-p8_3rdparty-dist_in1k-384px',
    'xcit-medium-24-p8_3rdparty_in1k', 'xcit-nano-12-p16_3rdparty-dist_in1k',
    'xcit-nano-12-p16_3rdparty-dist_in1k-384px', 'xcit-nano-12-p16_3rdparty_in1k',
    'xcit-nano-12-p8_3rdparty-dist_in1k', 'xcit-nano-12-p8_3rdparty-dist_in1k-384px',
    'xcit-nano-12-p8_3rdparty_in1k', 'xcit-small-12-p16_3rdparty-dist_in1k',
    'xcit-small-12-p16_3rdparty-dist_in1k-384px', 'xcit-small-12-p16_3rdparty_in1k',
    'xcit-small-12-p8_3rdparty-dist_in1k', 'xcit-small-12-p8_3rdparty-dist_in1k-384px',
    'xcit-small-12-p8_3rdparty_in1k', 'xcit-small-24-p16_3rdparty-dist_in1k',
    'xcit-small-24-p16_3rdparty-dist_in1k-384px', 'xcit-small-24-p16_3rdparty_in1k',
    'xcit-small-24-p8_3rdparty-dist_in1k', 'xcit-small-24-p8_3rdparty-dist_in1k-384px',
    'xcit-small-24-p8_3rdparty_in1k', 'xcit-tiny-12-p16_3rdparty-dist_in1k',
    'xcit-tiny-12-p16_3rdparty-dist_in1k-384px', 'xcit-tiny-12-p16_3rdparty_in1k',
    'xcit-tiny-12-p8_3rdparty-dist_in1k', 'xcit-tiny-12-p8_3rdparty-dist_in1k-384px',
    'xcit-tiny-12-p8_3rdparty_in1k', 'xcit-tiny-24-p16_3rdparty-dist_in1k',
    'xcit-tiny-24-p16_3rdparty-dist_in1k-384px', 'xcit-tiny-24-p16_3rdparty_in1k',
    'xcit-tiny-24-p8_3rdparty-dist_in1k', 'xcit-tiny-24-p8_3rdparty-dist_in1k-384px',
    'xcit-tiny-24-p8_3rdparty_in1k'
]