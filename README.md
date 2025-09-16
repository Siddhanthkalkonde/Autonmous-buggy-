# YOLOv8 Semantic Segmentation 🎨

> *When regular object detection is too mainstream and you need to color inside the lines* 🖍️

A absolutely fire real-time semantic segmentation system that makes everything look like a heat map because why settle for boring bounding boxes when you can have COLORS? This beast uses YOLOv8n-seg to paint your world in rainbow mode. 🌈

## Features That Absolutely Slap

- 🎨 **Real-time semantic segmentation** - Because pixels deserve individual attention
- 🌈 **Color-coded masks** - Making everything look like a trippy art piece
- 📹 **Live camera feed** - Stream your segmented reality
- 🎬 **Video file support** - Process pre-recorded content like a pro
- 🔥 **Heat map vibes** - JET colormap because we're fancy like that

## Requirements (Don't Skip This Part)

Install these or prepare to cry:

```bash
pip install ultralytics      # The segmentation overlord
pip install opencv-python    # Computer vision OG
pip install numpy            # Because math is inevitable
```

## Usage (Time to Get Segmenting)

### Basic Commands That Actually Work

```bash
# Live camera segmentation (the classic)
python your_script.py

# That's it. No fancy args needed. We keep it simple.
```

### Want to Process Videos Instead?

Just uncomment this line in the code and flex with your video files:

```python
# Swap this line:
cap = cv2.VideoCapture(0)

# With this fire:
cap = cv2.VideoCapture('/path/to/your/epic/video.mp4')
```

## Model Setup (The Foundation)

The code uses `yolov8n-seg.pt` which should be in your working directory:

1. **If you don't have it**: The script will download it automatically (ultralytics is smart like that)
2. **If you have a custom model**: Update this line like a boss:
```python
model_path = 'your_custom_segmentation_model.pt'
```

## How This Absolute Unit Works

1. **Model Loading** 🚀: Loads YOLOv8n segmentation model (the good stuff)
2. **Frame Processing** 🎨: Takes each frame and goes full Picasso on it
3. **Mask Creation** 🎭: Creates pixel-perfect segmentation masks
4. **Color Magic** 🌈: Applies JET colormap because we're not basic
5. **Blending** ✨: Mixes original frame with colorful mask (chef's kiss)

## Controls (Keep It Simple)

- **'q' key**: Quit like a civilized human being
- **Close window**: Also works if you're feeling fancy

## Code Breakdown (For the Nerds)

- `load_model()` - Loads the segmentation beast
- `process_frame()` - Where the magic happens (literally paints pixels)
- `main()` - The director of this whole show

## What You'll Actually See

Prepare your eyeballs for:
- Live video feed that looks like thermal imaging
- Objects outlined in rainbow colors
- Everything looking like you're viewing through alien vision
- Smooth 640x480 performance (because we're not trying to fry your GPU)

## Customization Options (Make It Yours)

### Change Resolution (If Your PC Can Handle It)
```python
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)   # Go bigger
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Go harder
```

### Switch Colormap (Because Options)
```python
# Instead of COLORMAP_JET, try:
cv2.COLORMAP_HOT      # Fire vibes
cv2.COLORMAP_COOL     # Ice cold
cv2.COLORMAP_RAINBOW  # Full spectrum chaos
```

### Adjust Blending (Control the Vibe)
```python
# Current: 60% original, 40% mask
blended = cv2.addWeighted(frame, 0.6, color_mask, 0.4, 0)

# Want more mask? Go wild:
blended = cv2.addWeighted(frame, 0.3, color_mask, 0.7, 0)
```

## Troubleshooting (When Reality Hits)

**No segmentation masks showing up?**
- Your objects might be too basic for the model to care about

**Camera not working?**
- Check if something else is hogging your webcam (looking at you, Zoom)

**Low FPS/laggy performance?**
- Lower the resolution or get better hardware (harsh but true)

**Model downloading forever?**
- Your internet might be slower than dial-up

## Performance Tips (Pro Mode)

- **Stick to 640x480** unless you have a beast setup
- **Close other apps** hogging your CPU/GPU
- **Use GPU acceleration** if you have CUDA setup
- **Process every nth frame** if you're still struggling

## Fun Facts

- This uses the "nano" version (yolov8n-seg) so it won't murder your computer
- JET colormap makes everything look like predator vision
- Semantic segmentation is just object detection with commitment issues

---

**Built by someone who thinks regular bounding boxes are for peasants** 🎨💻

*P.S. - If this makes your computer sound like a jet engine, that's normal. If it starts smoking, that's not.* 🔥

*Last updated: When we remembered segmentation is cooler than detection*
