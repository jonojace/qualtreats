# survey_id should remain unchanged
survey_id = "SV_4TLSPrwNIjymdh3"

# the below variables should be set according to your survey specifications

# this text will appear in each question
ab_question_text = "Which of the following two renditions of '{}' are closer to the reference recording in terms of pronunciation?"
mc_question_text= "Are there any errors in this speech sample?"
trs_question_text = "Please type the sentence you hear in this audio sample."
mushra_question_text = "How natural are the following speech recordings? <br> Reference: "
mos_question_text = "Listen to this speech sample, then rate the quality of the speech."
# the answer options for multiple choice questions
mc_choice_text = ['Yes', 'No']

# these files should contain the urls to be embedded in questions/choices
# each file should have a filename and url per line, separated by whitespace
# ab_file1 = "resources/ab-urls-1.txt"
# ab_file2 = "resources/ab-urls-2.txt"
# ab_targetwords = "resources/ab-targetwords.txt"
abc_file1 = "resources/abc-urls-1.txt"
abc_file2 = "resources/abc-urls-2.txt"
abc_file3 = "resources/abc-urls-3.txt"
mc_file = "resources/mc-urls.txt"
trs_file = "resources/trs-urls.txt"
mos_file = "resources/mos-urls.txt"

# IS 2022 ab urls (have 6 tests!)
# ab_file1 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test1_a.txt"
# ab_file2 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test1_b.txt"
# ab_targetwords = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test1_targetwords.txt"
# ab_file1 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test2_a.txt"
# ab_file2 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test2_b.txt"
# ab_targetwords = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test2_targetwords.txt"
# ab_file1 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test3_a.txt"
# ab_file2 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test3_b.txt"
# ab_targetwords = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test3_targetwords.txt"
# ab_file1 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test4_a.txt"
# ab_file2 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test4_b.txt"
# ab_targetwords = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test4_targetwords.txt"
# ab_file1 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test5_a.txt"
# ab_file2 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test5_b.txt"
# ab_targetwords = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test5_targetwords.txt"
# ab_file1 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test6_a.txt"
# ab_file2 = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test6_b.txt"
# ab_targetwords = "IS2022_speech_audio_corrector_ab_urls/ab-urls-test6_targetwords.txt"

# SSW 2023 
ab_file1 = "SSW2023_ASR_spellings/ab-urls-test1_a.txt"
ab_file2 = "SSW2023_ASR_spellings/ab-urls-test1_b.txt"
ab_targetwords = "SSW2023_ASR_spellings/ab-urls-test1_targetwords.txt"

# mushra filenames should be the same across folders
# audiofile urls should vary only by folder name
# any number of folders can be specified
mushra_files = "resources/mushra-urls.txt"
mushra_root = "https://groups.inf.ed.ac.uk/cstr3/cvbotinh/Mushra_example/samples"
# the hidden reference folder should be included in both mushra_folders and mushra_ref_folder
mushra_folders = ["G1","G1H","G1HA","G1TH", "G1THA"]
mushra_ref_folder = "G1THA"

# MC questions have sentence text embedded
# this file should have a filename and corresponding sentence string per line
mc_sentence_file = "resources/sentences.txt"
