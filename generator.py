from transformers import AutoProcessor, MusicgenForConditionalGeneration

def generate_audio(prompt, duration=10):
  processor = AutoProcessor.from_pretrained("facebook/musicgen-large")
  model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-large")

  inputs = processor(
      text = [prompt],
      padding = True,
      return_tensors = "pt"    
  )

  duration = duration/5

  tokens = int(256*duration)

  audio_values = model.generate(**inputs, max_new_tokens=tokens)
  sampling_rate = model.config.audio_encoder.sampling_rate

  audio_array = audio_values[0].cpu().numpy()

  return audio_array, sampling_rate