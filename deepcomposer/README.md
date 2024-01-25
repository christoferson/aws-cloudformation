

# Generative AI algorithms
Generative AI is a broad category of algorithms, the most popular of which include Generative Adversarial Networks (GANs), Variational Autoencoders (VAEs) and Autoregressive (AR) Models.


# Generative adversarial networks
Generative Adversarial Networks (GANs) are a type of machine learning network in which two neural networks compete. One network is tasked with generating realistic-seeming content (unsupervised learning), while the other network is tasked with distinguishing the generated content against real data (supervised learning).

# The generator
The generator within a GAN is a machine learning model that's trained to produce realistic-seeming output.
The Generator is like an orchestra — it trains, practises, and tries to generate polished music.

# The discriminator
The discriminator is another machine learning model which is trained to take an input and classify whether or not the input is real or generated.

The discriminator is like the orchestra's conductor — it judges the quality of the output and tries to achieve the style of music that it has been trained on.

# Steps

Content generation
Initially, the generator produces content samples based on random inputs.

Classifying content
The discriminator looks for features (e.g. tempo) from the dataset it was trained on (e.g. Pop, Rock, Classical) in the content samples the generator created. It decides whether or not the content samples belong in the training set.

Generative AI algorithms
Generative AI is a broad category of algorithms, the most popular of which include Generative Adversarial Networks (GANs), Variational Autoencoders (VAEs) and Autoregressive (AR) Models.

Generative adversarial networks
Generative Adversarial Networks (GANs) are a type of machine learning network in which two neural networks compete. One network is tasked with generating realistic-seeming content (unsupervised learning), while the other network is tasked with distinguishing the generated content against real data (supervised learning).

The generator
The generator within a GAN is a machine learning model that's trained to produce realistic-seeming output.

The Generator is like an orchestra — it trains, practises, and tries to generate polished music.

The discriminator
The discriminator is another machine learning model which is trained to take an input and classify whether or not the input is real or generated.

The discriminator is like the orchestra's conductor — it judges the quality of the output and tries to achieve the style of music that it has been trained on.

Content generation
Initially, the generator produces content samples based on random inputs.

Classifying content
The discriminator looks for features (e.g. tempo) from the dataset it was trained on (e.g. Pop, Rock, Classical) in the content samples the generator created. It decides whether or not the content samples belong in the training set.

Training GANs
The results of the discriminator's judgements are used to train both models. The generator is trained to optimize for producing realistic content that the discriminator cannot distinguish from the real samples. Meanwhile, the discriminator is trained to increase its ability to detect generated content.

This back-and-forth behavior, where the two models are directly competing against each other, is the adversarial part of GANs.

# Introduction to computer music
For a machine learning model to be able to interpret and generate music, it's important to represent music in a format which preserves the precise details of how the music is played.

Instead of processing a sound file, machine learning models such as those used in AWS DeepComposer examine those details to faithfully reproduce instruments and musical styles.

# Pitch
Pitch is a tone that is assigned a relative position on a musical scale. Each note is assigned a numeric value, starting at 0 for the lowest possible note, and ranging up to 127 for the highest.

The keys on the AWS DeepComposer keyboard range from 41 to 72. The Octave Adjust buttons shift the pitch values up or down in multiples of 12 to play higher or lower pitches.

# Velocity
Velocity encodes how hard a single note is pressed. Pressing the key faster results in a higher value for the velocity, which creates a louder sound. Velocity values range from 1 (minimum, practically inaudible) to 127 (maximum).

# Tempo
Tempo describes how fast music is played. Music typically follows a certain beat or meter, which drives the rhythm of the notes played. The speed of this beat is measured in beats per minute. A higher number of beats per minute corresponds to a faster playback speed (tempo).

# MIDI
The MIDI file format is an industry-standard used by computers to record and store music. The file format encodes details such as playback tempo, which instruments are used, and a series of events that encode a note being pressed or released, including the pitch and velocity of the note.
