
import pandas as pd

#Participant 1
df = pd.read_csv("Gayatri.csv")
print(df.head())
df = df.drop(columns=[
    "mouse.x", "mouse.y", "mouse.leftButton", "mouse.midButton",
    "mouse.rightButton", "mouse.time",
    "trials_2.mouse.x", "trials_2.mouse.y",
    "trials_2.mouse.leftButton", "trials_2.mouse.midButton",
    "trials_2.mouse.rightButton", "trials_2.mouse.time",
    "textbox.text", "button.numClicks", "button.timesOn",
    "button.timesOff", "trials_2.textbox.text",
    "trials_2.button.numClicks", "trials_2.button.timesOn",
    "trials_2.button.timesOff",
    "trial.started", "trial.stopped", "instructions.started",
    "key_resp.started", "math_section.started",
    "math_section.stopped", "memm.started", "memm.stopped",
    "text.started", "textbox.started", "button.started",
    "mouse.started", "performance.started", "performance.stopped",
    "routine_1.started", "routine_1.stopped",
    "thanks.started", "thanks.stopped",
    "trials_2.thisRepN", "trials_2.thisTrialN",
    "trials_2.thisN", "trials_2.thisIndex",
    "trials_2.key_resp_4.keys", "trials_2.key_resp_4.corr",
    "trials_2.key_resp_4.rt", "trials_2.key_resp_4.duration",
    "key_resp.keys", "key_resp.rt", "key_resp.duration",
    "key_resp_4.duration", "thisN", "thisRow.t",
    "notes", "piloting", "psychopyVersion", "frameRate",
    "expName", "expVersion", "expStart", "date", "text_8.started", "text_7.started", "text_2.stopped", "text_7.started", "text_2.started"
], errors="ignore")

print(df.mean(numeric_only=True))

mean_correct = df["key_resp_4.corr"].mean()

print(f"the mean correct trials of gayatri is: {mean_correct: .2f}")

percent_correct = mean_correct*100
print(f"the percent correct trials of gayatri is: {percent_correct: .2f}%")

mean_rt = df["key_resp_4.rt"].mean()
print(f"the mean reaction time of gayatri is: {mean_rt:.2f} seconds")


#Participant 2

df = pd.read_csv("ShekherMaini.csv")
print(df.head())
df = df.drop(columns=[
    "mouse.x", "mouse.y", "mouse.leftButton", "mouse.midButton",
    "mouse.rightButton", "mouse.time",
    "trials_2.mouse.x", "trials_2.mouse.y",
    "trials_2.mouse.leftButton", "trials_2.mouse.midButton",
    "trials_2.mouse.rightButton", "trials_2.mouse.time",
    "textbox.text", "button.numClicks", "button.timesOn",
    "button.timesOff", "trials_2.textbox.text",
    "trials_2.button.numClicks", "trials_2.button.timesOn",
    "trials_2.button.timesOff",
    "trial.started", "trial.stopped", "instructions.started",
    "key_resp.started", "math_section.started",
    "math_section.stopped", "memm.started", "memm.stopped",
    "text.started", "textbox.started", "button.started",
    "mouse.started", "performance.started", "performance.stopped",
    "routine_1.started", "routine_1.stopped",
    "thanks.started", "thanks.stopped",
    "trials_2.thisRepN", "trials_2.thisTrialN",
    "trials_2.thisN", "trials_2.thisIndex",
    "trials_2.key_resp_4.keys", "trials_2.key_resp_4.corr",
    "trials_2.key_resp_4.rt", "trials_2.key_resp_4.duration",
    "key_resp.keys", "key_resp.rt", "key_resp.duration",
    "key_resp_4.duration", "thisN", "thisRow.t",
    "notes", "piloting", "psychopyVersion", "frameRate",
    "expName", "expVersion", "expStart", "date", "text_8.started", "text_7.started", "text_2.stopped", "text_7.started", "text_2.started"
], errors="ignore")

print(df.mean(numeric_only=True))

mean_correct = df["key_resp_4.corr"].mean()
print(f"the mean correct trials of ShekherMaini is: {mean_correct:.2f}")
percent_correct = mean_correct*100
print(f"the percent correct trials of ShekherMaini is: {percent_correct:.2f}% ")

mean_rt = df["key_resp_4.rt"].mean()
print(f"the mean reaction time of ShekherMaini is: {mean_rt:.2f} seconds")

#participant 3

df = pd.read_csv("Alisha.csv")
print(df.head())
df = df.drop(columns=[
    "mouse.x", "mouse.y", "mouse.leftButton", "mouse.midButton",
    "mouse.rightButton", "mouse.time",
    "trials_2.mouse.x", "trials_2.mouse.y",
    "trials_2.mouse.leftButton", "trials_2.mouse.midButton",
    "trials_2.mouse.rightButton", "trials_2.mouse.time",
    "textbox.text", "button.numClicks", "button.timesOn",
    "button.timesOff", "trials_2.textbox.text",
    "trials_2.button.numClicks", "trials_2.button.timesOn",
    "trials_2.button.timesOff",
    "trial.started", "trial.stopped", "instructions.started",
    "key_resp.started", "math_section.started",
    "math_section.stopped", "memm.started", "memm.stopped",
    "text.started", "textbox.started", "button.started",
    "mouse.started", "performance.started", "performance.stopped",
    "routine_1.started", "routine_1.stopped",
    "thanks.started", "thanks.stopped",
    "trials_2.thisRepN", "trials_2.thisTrialN",
    "trials_2.thisN", "trials_2.thisIndex",
    "trials_2.key_resp_4.keys", "trials_2.key_resp_4.corr",
    "trials_2.key_resp_4.rt", "trials_2.key_resp_4.duration",
    "key_resp.keys", "key_resp.rt", "key_resp.duration",
    "key_resp_4.duration", "thisN", "thisRow.t",
    "notes", "piloting", "psychopyVersion", "frameRate",
    "expName", "expVersion", "expStart", "date", "text_8.started", "text_7.started", "text_2.stopped", "text_7.started", "text_2.started"
], errors="ignore")

print(df.mean(numeric_only=True))
mean_correct = df["key_resp_4.corr"].mean()
print(f"the mean correct trials of Alisha is: {mean_correct:.2f}")
percent_correct = mean_correct*100
print(f"the percent correct trials of Alisha is: {percent_correct:.2f}% ")

mean_rt = df["key_resp_4.rt"].mean()

print(f"the mean reaction time of Alisha is: {mean_rt:.2f} seconds")


#grouped data analysis
import glob
data_total = ["Alisha.csv", "Gayatri.csv", "ShekherMaini.csv"]
big_data = []
for data in data_total:
    df = pd.read_csv(data)
    big_data.append(df)
big_data = pd.concat(big_data, ignore_index=True)
print(big_data.tail())
big_data = big_data.drop(columns=[
    "mouse.x", "mouse.y", "mouse.leftButton", "mouse.midButton",
    "mouse.rightButton", "mouse.time",
    "trials_2.mouse.x", "trials_2.mouse.y",
    "trials_2.mouse.leftButton", "trials_2.mouse.midButton",
    "trials_2.mouse.rightButton", "trials_2.mouse.time",
    "textbox.text", "button.numClicks", "button.timesOn",
    "button.timesOff", "trials_2.textbox.text",
    "trials_2.button.numClicks", "trials_2.button.timesOn",
    "trials_2.button.timesOff",
    "trial.started", "trial.stopped", "instructions.started",
    "key_resp.started", "math_section.started",
    "math_section.stopped", "memm.started", "memm.stopped",
    "text.started", "textbox.started", "button.started",
    "mouse.started", "performance.started", "performance.stopped",
    "routine_1.started", "routine_1.stopped",
    "thanks.started", "thanks.stopped",
    "trials_2.thisRepN", "trials_2.thisTrialN",
    "trials_2.thisN", "trials_2.thisIndex",
    "trials_2.key_resp_4.keys", "trials_2.key_resp_4.corr",
    "trials_2.key_resp_4.rt", "trials_2.key_resp_4.duration",
    "key_resp.keys", "key_resp.rt", "key_resp.duration",
    "key_resp_4.duration", "thisN", "thisRow.t",
    "notes", "piloting", "psychopyVersion", "frameRate",
    "expName", "expVersion", "expStart", "date", "text_8.started", "text_7.started", "text_2.stopped", "text_7.started", "text_2.started"
], errors="ignore")
print(big_data.mean(numeric_only=True))

avg_correct_all_3_participants = big_data["key_resp_4.corr"].mean()
print(f"mean correct trials across the 3 participants is: {avg_correct_all_3_participants:.2f}")

percent_correct_all_3_participants = avg_correct_all_3_participants*100
print(f"percent correct trials across the 3 participants is: {percent_correct_all_3_participants:.2f}%)")

avg_rt_all_3_participants = big_data["key_resp_4.rt"].mean()
print(f"mean reaction time across the 3 participants is {avg_rt_all_3_participants:.2f} seconds")

