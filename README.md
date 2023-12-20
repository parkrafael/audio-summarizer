# Audio Summarizer 

Using OpenAI's Whisper-1 and GPT-3.5 this Python program allows user to upload audio (mp3, wav, m4a) files and obtain summarized notes of the recording.

## Development Setup:
- Run `pip install openai pydub dotenv`
- Create `.env` file and initialize OpenAI key
- Run `python summary.py` to start the program


## Test Examples:

### "organic.mp3"
*****Original Audio:** https://www.youtube.com/watch?v=DTKKSyooqyM***

- Carbon-carbon single bonds, double bonds, and triple bonds are known as alkanes, alkenes, and alkynes, respectively
- Alkanes and single bonds between carbons do not count as functional groups, as they serve as the carbon backbone
- A six-membered ring with alternating single and double bonds is called a benzene ring
- Directly attached benzene rings are called phenyl, one carbon away is called benzyl
- Adding heteroatoms with a single bond to carbons creates different functional groups
- Heteroatoms like halogens, nitrogen-containing groups, and hydroxyl groups result in alkyl halides, amines, and alcohols, respectively
- Replacing the O in an alcohol with an R group creates an ether, and with an S creates a thiol
- A C triple bond N becomes a nitrile as a functional group
- Carbonyls (C double bond O) are not functional groups but can become functional groups depending on what they are attached to
- If attached to carbon chain, carbonyls are called aldehydes or ketones, depending on location

#### Original audio length: 4:15 minutes
#### Time taken to finish: 0:49 minutes

### "phil.mp3"
*****Original Audio:** https://www.learnoutloud.com/Free-Audio-Video/Philosophy/Ancient-and-Medieval-Philosophy/What-is-Knowledge/31329***

- The Modern Scholar series is introduced by Richard Davidson
- The course is called "Discovering the Philosopher in You, the Big Questions in Philosophy" and is taught by Colin McGinn
- Philosophy explores fundamental questions about the nature of the world, ethics, the self, free will, and the existence of God
- The course will approach these questions from both a historical and scientific perspective
- The goal is to uncover and exercise the philosopher's mind within each individual
- Skepticism is introduced as a philosophical problem, questioning what we really know
- Descartes' skepticism and the problem of other minds are discussed
- The problem of induction and the problem of the past are also raised
- The limits of skepticism and the importance of knowledge are explored
- The consequences of skepticism are discussed, including the idea of metaphysical solitary confinement
- The next lecture will focus on defining and analyzing knowledge.

#### Original audio length: 38:57 minutes
#### Time taken to finish: 6:30 minutes
