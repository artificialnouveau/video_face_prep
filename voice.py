#%%
# !pip install pydub imblearn pyAudioAnalysis hmmlearn eyed3 plotly

#%%
from pydub import AudioSegment
from tqdm import tqdm
import os
import gc

def extract_speaker_segments(wav_filename, num_speakers=2):
    # Perform speaker diarization using the provided function
    flags, _, _ = aS.speaker_diarization(wav_filename, num_speakers)

    # Load the audio file using pydub
    audio = AudioSegment.from_wav(wav_filename)

    # Extract segments for each speaker
    segments = []
    sampling_rate = 0.1  
    for speaker_num in tqdm(set(flags), desc="Processing Speakers", unit="speaker"):
        start_time = None
        end_time = None
        for idx, speaker in enumerate(flags):
            if speaker == speaker_num:
                if start_time is None:
                    start_time = idx * sampling_rate * 1000  # convert to ms
                end_time = (idx + 1) * sampling_rate * 1000
            elif start_time is not None:
                segments.append((start_time, end_time, speaker_num))
                start_time = None

        if start_time is not None:
            segments.append((start_time, end_time, speaker_num))

    # Save each segment
    temp_files = []
    for idx, (start, end, speaker_num) in tqdm(enumerate(segments), desc="Saving Segments", unit="segment"):
        segment_audio = audio[start:end]
        segment_filename = f"{wav_filename[:-4]}_speaker{speaker_num}_segment{idx}.wav"
        segment_audio.export(segment_filename, format="wav")
        temp_files.append(segment_filename)

    # Merge all segments with the same speaker number
    output_segments = []
    for speaker_num in tqdm(set(flags), desc="Merging Segments", unit="merge"):
        segments_to_merge = [f for f in temp_files if f"_speaker{speaker_num}_" in f]
        merged_audio = AudioSegment.empty()
        for seg_file in segments_to_merge:
            merged_audio += AudioSegment.from_wav(seg_file)
        merged_filename = f"{wav_filename[:-4]}_merged_speaker{speaker_num}.wav"
        merged_audio.export(merged_filename, format="wav")
        output_segments.append(merged_filename)

    # Delete all segment files
    for file in os.listdir('.'):
        if "segment" in file:
            os.remove(file)

    return output_segments



#%%
extract_speaker_segments(r"path_to_your_file.wav")
