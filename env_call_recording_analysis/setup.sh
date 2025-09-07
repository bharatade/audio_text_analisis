#!/bin/bash
set -e

# Define directories
NEMO_DIR="./NeMo"
MODEL_DIR="./models"
mkdir -p $MODEL_DIR

# Install Python dependencies
echo "🔹 Installing Python dependencies..."
pip install -r requirements.txt --quiet --extra-index-url https://download.pytorch.org/whl/cu124

# Install ffmpeg
echo "🔹 Installing ffmpeg..."
apt-get update -y && apt-get install -y ffmpeg

# Clone NeMo if not already present
if [ ! -d "$NEMO_DIR" ]; then
    echo "🔹 Cloning NeMo repository..."
    git clone https://github.com/AI4Bharat/NeMo.git
    cd NeMo
    bash reinstall.sh
    cd ..
else
    echo "✅ NeMo repository already exists."
fi

# Download pretrained models
echo "🔹 Downloading models..."
declare -A model_urls=(
  ["indicconformer_stt_as_hybrid_rnnt_large.nemo"]="https://objectstore.e2enetworks.net/indicconformer/models/indicconformer_stt_as_hybrid_rnnt_large.nemo"
  ["indicconformer_stt_mr_hybrid_rnnt_large.nemo"]="https://objectstore.e2enetworks.net/indicconformer/models/indicconformer_stt_mr_hybrid_rnnt_large.nemo"
  ["indicconformer_stt_hi_hybrid_rnnt_large.nemo"]="https://objectstore.e2enetworks.net/indicconformer/models/indicconformer_stt_hi_hybrid_rnnt_large.nemo"
)

for fname in "${!model_urls[@]}"; do
    fpath="$MODEL_DIR/$fname"
    if [ ! -f "$fpath" ]; then
        echo "Downloading $fname..."
        wget -q -O "$fpath" "${model_urls[$fname]}"
    else
        echo "✅ $fname already exists."
    fi
done

echo -e "\n✅ Setup complete. Please restart your kernel or environment."
