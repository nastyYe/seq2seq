
seq2seq model
=====================================================
Requirements
--------------------------------------
- python 3.6
- TensorFlow 1.5.0

example:

    source /home/miproj/urop.2018/pm574/anaconda3/bin/activate tf_gpu

Encoder&Decoder for GED/GEC experiments
--------------------------------------
Training:

    python train.py \
        --train_src lib/data/source.txt \
        --train_tgt lib/data/target.txt \
        --vocab_src lib/wlists/source.txt \
        --vocab_tgt lib/wlists/target.txt \
        --embedding_size 200 \
        --num_layers 2 \
        --dropout 0.2 \
        --num_units 128 \
        --learning_rate 0.001 \
        --batch_size 256 \
        --num_epochs 100 \
        --random_seed 25 \
        --decoding_method greedy \
        --max_sentence_length 32 \
        --use_gpu True \
        --save lib/models/tmp0

Translating:

    python translate.py \
        --load lib/models/tmp0 \
        --srcfile lib/srcfile.txt \ 
        --tgtfile lib/tgtfile.txt \ 
        --model_number 19
