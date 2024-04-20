# Investigating Prompt-Induced Bias in GPT-3.5 Turbo Responses within Digital Forensics

This repository contains experiments that we performed on
the [Honeynet challenge 3 "Banking Troubles"](https://www.honeynet.org/challenges/forensic-challenge-3-banking-troubles/)
dataset and their results.

Experiments were performed on the questions 1, 2, 7 and 9 of the original challenge. Questions were prompted to the
GPT-3.5 Turbo model using the OpenAI API.

In each case the original question was kept as a baseline and multiple biased questions were constructed to evaluate
the model's susceptibility to bias in the prompts.

For each question additional context was produced by
running [volatility](https://github.com/volatilityfoundation/volatility) against the memory dump provided in the
challenge.

Datasets for different Honeynet challenges can be found here:
https://github.com/honeynet/forensic_challenges/tree/master

To execute experiments locally, make sure to have a `OPENAI_API_KEY` environment variable set with your OpenAI API key.
