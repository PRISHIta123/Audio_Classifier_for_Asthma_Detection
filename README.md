# Audio_Classifier_for_Asthma_and_Hypothorax_Detection
This project classifies audio samples collected from patients, including their cough, fluid levels and wheezing frequencies in real time to detect asthma and hypothorax conditions.

Process for Connecting, Configuring and Testing microphone connected to R Pi:
https://developers.google.com/assistant/sdk/guides/service/python/embed/setup

Steps for Interfacing ADC converter MCP3008 with R Pi:
https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi?view=all

Workflow:
1. Connect microphone to R Pi using Linux commands
2. Connect adc converter to R pi and configure it using steps and python code
3. Insert SD card with trained model
4. Test if microphone signals are being received by R pi and pass analog signals to adc converter
5. Filter audio using Matlab code (chebyshev filters)
6. Segment filtered audio at regular intervals to match test clip time with training clip time
7. Pass test clips through trained classifier to predict output (detected diseases if any) by calling the trained model from matlab

Link to Stacked CNN for Training:
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8605515

Link to Hybrid Classifier for Training(SVM + ANN):
http://downloads.hindawi.com/journals/mpe/2015/209814.pdf

Other traditional algorithms: SVM, GNN(Gaussian Neural Netwroks), ELM (Extreme Learning Machine)
