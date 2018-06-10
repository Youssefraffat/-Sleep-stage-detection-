# -Sleep-stage-detection-
Implementing signal processing techniques using Python programming language to detect the sleep stage based on a real EEG dataset.


## Why do neuroscientists create hypnograms?
Sleep researchers classify sleep into multiple stages based on various physiological
characteristics including eye movements (detected by electrooculography, EOG), muscle tone
(detected by electromyography, EMG), and neural activity (detected by EEG). These stages
include both rapid eye movement (REM) and non-rapid eye movement (NREM) sleep. NREM
sleep can be further divided into three or four categories based on specific EEG activity patterns.
Hypnograms are useful tools to visualize how sleep stages change throughout the night. In
general, a night of sleep consists of multiple sleep cycles about 90 minutes in duration. Early
cycles have the most slow wave sleep (SWS - the deepest levels of NREM sleep) while later
cycles have the most REM sleep, and may even include periods of wakefulness. Hypnogram
analysis may indicate disrupted sleep resulting from various medical conditions or disorders or
as a side-effect from various drugs.
Hypnograms are traditional constructed by visual inspection of the physiological signals.
Researchers classify sleep in 30 second epochs based on criteria original standardize by
Rectshaffen and Kales in 19681 and revised by the American Academy of Sleep Medicine
(AASM) in 20072. This process is often completed manually, although there are some examples
of algorithms that classify the physiological activity. In this problem set, you will create an
algorithm that attempts to classify sleep state based on EEG activity. You will also generate
visualizations of EEG data including hypnograms.

## neuroscientists use automatic classifiers?
Neuroscientists often seek to “decode” the neural signal recorded during experiments. The
purpose of this decoding may be to understand how the neural activity relates to overall brain
state or human behavior (as in this problem set), or the purpose of decoding may be to drive
neuroprosthetic devices (as we learned about from Dr. Donoghue). Classifiers are simply
algorithms that attempt to assign meaning (in our case, sleep stages) to activity.
In this problem set, we will guide you to complete a simple classifier. Because the classifier will
be quite simple, its performance may not be that high. Neuroscientists often apply technically
advanced machine learning techniques to build classifiers of neural activity. 
Some machine learning algorithms learn to classify data in a “supervised” way by learning from data that has been pre-classified (for example, by the human researchers who developed our data set.). The algorithm will create a classifier that can then be applied to new data. Other algorithms seek to find the different groups or clusters of data within the existing set in an “unsupervised” manner and then classify data into these groups. These types of machine learning techniques are outside the scope of this course, but if you have background experience with machine learning you are welcome to apply them here or in the final project for the course.
