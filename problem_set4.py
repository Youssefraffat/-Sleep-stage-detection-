#
#  NAME
#    problem_set4.py
#
#  DESCRIPTION
#    In Problem Set 4, you will classify EEG data into NREM sleep stages and
#    create spectrograms and hypnograms.
#
from __future__ import division
import numpy as np
import matplotlib.pylab as plt
import matplotlib.mlab as m


def load_examples(filename):
    """
    load_examples takes the file name and reads in the data.  It returns an
    array containing the 4 examples of the 4 stages in its rows (row 0 = REM;
    1 = stage 1 NREM; 2 = stage 2; 3 = stage 3 and 4) and the sampling rate for
    the data in Hz (samples per second).
    """
    data = np.load(filename)
    return data['examples'], int(data['srate'])

def load_eeg(filename):
    """
    load_eeg takes the file name and reads in the data.  It returns an
    array containing EEG data and the sampling rate for
    the data in Hz (samples per second).
    """
    data = np.load(filename)
    return data['eeg'], int(data['srate'])

def load_stages(filename):
    """
    load_stages takes the file name and reads in the stages data.  It returns an
    array containing the correct stages (one for each 30s epoch)
    """
    data = np.load(filename)
    return data['stages']

def plot_example_psds(example,rate):
    """
    This function creates a figure with 4 lines to show the overall psd for 
    the four sleep examples. (Recall row 0 is REM, rows 1-3 are NREM stages 1,
    2 and 3/4)
    """

    pxx_max_1=[]
    pxx_max_2=[]
    pxx_max_3=[]
    
   
    example_1_max=[]
    example_2_max=[]    
    example_3_max=[]    
    
    example_1_min=[]
    example_2_min=[]    
    example_3_min=[]        
    
    
    pxx0,freq0= m.psd(example[0],256,srate)   
    pxx1,freq1=m.psd(example[1],256,srate)
    pxx2,freq2=m.psd(example[2],256,srate)
    pxx3,freq3=m.psd(example[3],256,srate)
    pxx0_normalized=pxx0/sum(pxx0)
    pxx1_normalized=pxx1/sum(pxx1)
    pxx2_normalized=pxx2/sum(pxx2)
    pxx3_normalized=pxx3/sum(pxx3)
    
    plt.figure()    
    plt.plot(freq0,pxx0_normalized,color='k',label='REM sleep')
    plt.plot(freq1,pxx1_normalized,color='r',label='st1 NREM sleep')
    plt.plot(freq2,pxx2_normalized,color='b',label='st2 NREM sleep')    
    plt.plot(freq3,pxx3_normalized,color='c',label='st3 NREM sleep')    
    plt.xlim(0,30)    
    plt.xlabel('frequency in (HZ)')
    plt.ylabel('Power Spectal Denisty (db/HZ) ')
    plt.title('Psds for 4 stages')         
    plt.legend(loc=0)    
    plt.show()    
    
    
   
  
    

    for i in range(10):
       start=i*3840
       end=(i+1)*3840
       pxx,freq=m.psd(example[1][start:end],rate )
       pxx_normalized=pxx/sum(pxx)
       pxx_max_1=np.append(pxx_max_1,max(pxx_normalized))
       example_1_max=np.append(example_1_max,max(example[1][start:end]))    
       example_1_min=np.append(example_1_min,min(example[1][start:end]))    
    print [max(example_1_min) , min(example_1_min), max(example_1_max) , min(example_1_max)
   , max(pxx_max_1) , min(pxx_max_1)]    
   
   
   
   
    for i in range(10):
       start=i*3840
       end=(i+1)*3840
       pxx,freq=m.psd(example[2][start:end],rate)
       pxx_normalized=pxx/sum(pxx)
       pxx_max_2=np.append(pxx_max_2,max(pxx_normalized))
       example_2_max=np.append(example_2_max,max(example[2][start:end]))    
       example_2_min=np.append(example_2_min,min(example[2][start:end]))    
    print [max(example_2_min) , min(example_2_min) , max(example_2_max) , min(example_2_max)   
     ,max(pxx_max_2) , min(pxx_max_2)]      
    
    
    
    for i in range(10):
       start=i*3840
       end=(i+1)*3840
       pxx,freq=m.psd(example[3][start:end],rate)
       pxx_normalized=pxx/sum(pxx)
       pxx_max_3=np.append(pxx_max_3,max(pxx_normalized))
       example_3_max=np.append(example_3_max,max(example[3][start:end]))    
       example_3_min=np.append(example_3_min,min(example[3][start:end]))    
    print[ max(example_3_min) , min(example_3_min) , max(example_3_max) , min(example_3_max), max(pxx_max_3) , min(pxx_max_3) ] 
    
    
    
    
# stage 1
"""
max xpp is between  0.29754945782683134 : 0.2117888345750413

max example[1] is between 62.500546835843537 : 39.042285568860379

min example[1] is between   -38.267113391021937 : -49.191964296427557
""" 
# stage 2
"""
max xpp is between    0.36925548655142104 : 0.21093244560026334

max example[1] is between 122.96626924998539: 57.994394713666402

min example[1] is between  -62.029132510260197 : -145.05305930131246 


"""    
    
# stage 3

"""
max xpp is between  0.56820449680688645 : 0.45047862769093255 

max example[1] is between 364.4167754174145, 190.45514452645946

min example[1] is between   -214.63767257237106, -372.00227461944871
""" 
    
    
    
def plot_example_spectrograms(example,rate):
    """
    This function creates a figure with spectrogram sublpots to of the four
    sleep examples. (Recall row 0 is REM, rows 1-3 are NREM stages 1,
    2 and 3/4)
    """
    plt.figure()
    plt.specgram(example[0],1024,rate)
    plt.specgram(example[1],1024,rate)
    plt.specgram(example[2],1024,rate)
    plt.specgram(example[3],1024,rate)
    plt.ylim(0,50)
    plt.xlabel('Time(S)')
    plt.ylabel('Frequency(HZ)')     
    plt.title('spectrpgrams for the different stages')    
    plt.show()
    
    return
      
def classify_epoch(epoch,rate):
      
 state =0   
 xpp_total,freq=m.psd(epoch,rate)
 xpp=xpp_total/sum(xpp_total)
 #print max(xpp) , max(epoch) ,min(epoch)
 
 if max(xpp)<=0.4 and max(xpp)>= 0.1:
       if max(epoch)<63  and max(epoch)>39:
           if min(epoch) >-50 and min(epoch)<-38 :
                state=1
           else:
                state=2
       else:
           state =2
 elif max(xpp)<=0.45 and max(xpp)>= 0.19:
       if max(epoch)<123 and max(epoch)> 57 :
           state=2
       else:
           state =3
 elif max(xpp)<0.65 and max(xpp)> 0.45  :
       state=3
    
    
 return state

def plot_hypnogram(eeg, stages, srate):
    """
    This function takes the eeg, the stages and sampling rate and draws a 
    hypnogram over the spectrogram of the data.
    """
    print stages ,len(stages)
    fig,ax1 = plt.subplots()  #Needed for the multiple y-axes
    
    #Use the specgram function to draw the spectrogram as usual
    ax1.specgram(eeg,2048 ,srate)
    #Label your x and y axes and set the y limits for the spectrogram
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('frequency (HZ)')
    ax1.set_ylim(0,30)
    ax2 = ax1.twinx() #Necessary for multiple y-axes
    
    #Use ax2.plot to draw the hypnogram.  Be sure your x values are in seconds
    #HINT: Use drawstyle='steps' to allow step functions in your plot
        
    ax2.plot(np.arange(0,30*len(stages),30),stages,drawstyle='steps') 
    #Label your right y-axis and change the text color to match your plot
    ax2.set_ylabel('NREM Stages',color='b')

 
    #Set the limits for the y-axis 
    ax2.set_ylim(0.5,3.5)
    #Only display the possible values for the stages
    ax2.set_yticks(np.arange(1,4))
    
    #Change the left axis tick color to match your plot
    for t1 in ax2.get_yticklabels():
        t1.set_color('b')
    
    #Title your plot    
    plt.title('Hypnogram _practice data')
    plt.show()
        
def classifier_tester(classifiedEEG, actualEEG):
    """
    returns percent of 30s epochs correctly classified
    """
    epochs = len(classifiedEEG)
    incorrect = np.nonzero(classifiedEEG-actualEEG)[0]
    percorrect = (epochs - len(incorrect))/epochs*100
    
    print 'EEG Classifier Performance: '
    print '     Correct Epochs = ' + str(epochs-len(incorrect))
    print '     Incorrect Epochs = ' + str(len(incorrect))
    print '     Percent Correct= ' + str(percorrect) 
    print 
    return percorrect
  
    
def test_examples(examples, srate):
    """
    This is one example of how you might write the code to test the provided 
    examples.
    """
    i = 0
    bin_size = 30*srate
    c = np.zeros((4,len(examples[1,:])/bin_size))
    while i + bin_size < len(examples[1,:]):
        for j in range(1,4):
            c[j,i/bin_size] = classify_epoch(examples[j,range(i,i+bin_size)],srate)
        i = i + bin_size
    
    totalcorrect = 0
    num_examples = 0
    for j in range(1,4):
        canswers = np.ones(len(c[j,:]))*j
        correct = classifier_tester(c[j,:],canswers)
        totalcorrect = totalcorrect + correct
        num_examples = num_examples + 1
    
    average_percent_correct = totalcorrect/num_examples
    print 'Average Percent Correct= ' + str(average_percent_correct) 
    return average_percent_correct

def classify_eeg(eeg,srate):
    """
    DO NOT MODIFY THIS FUNCTION
    classify_eeg takes an array of eeg amplitude values and a sampling rate and 
    breaks it into 30s epochs for classification with the classify_epoch function.
    It returns an array of the classified stages.
    """
    bin_size_sec = 30
    bin_size_samp = bin_size_sec*srate
    t = 0
    classified = np.zeros(len(eeg)/bin_size_samp)
    while t + bin_size_samp < len(eeg):
       classified[t/bin_size_samp] = classify_epoch(eeg[range(t,t+bin_size_samp)],srate)
       t = t + bin_size_samp
    return classified
        
##########################
#You can put the code that calls the above functions down here    
if __name__ == "__main__":
    #YOUR CODE HERE
    
    plt.close('all') #Closes old plots.
    
    ##PART 1
    #Load the example data
    examples,srate=load_examples('example_stages.npz')
    #Plot the psds
    plot_example_psds(examples,srate)
    #Plot the spectrograms
    plot_example_spectrograms(examples,srate)
    #Test the examples
    """
    for j in range(1,4):
        print ('')
        print ('Testing example  is state :' +str(j) )        
        for i in range(10):
            start=i*3840
            end=(i+1)*3840
            epoch=examples[j][start:end]
            print ('predicted NREM stage is : ' + str(classify_epoch(epoch,srate)) )
    """        
    #Load the practice data
    eeg, srate = load_eeg('practice_eeg.npz')
    
    #Load the practice answers
    stages = load_stages('practice_answers.npz')        
    #Classify the practice data
    classified=classify_eeg(eeg,srate)        
    print len(classified)
     
    #Check your performance
    classifier_tester(classified, stages)
    #Generate the hypnogram plots
    plot_hypnogram(eeg, stages, srate) 
    
    example,rate=load_eeg('test_eeg.npz')
    plot_hypnogram(example,classify_eeg(example,rate),rate)

