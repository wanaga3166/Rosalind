#!/usr/bin/python

S1="GCACGTTGGCGCGGAGGCTGCTTGAAAGGAGCCGGGAAGTGCTTATCCATTCACATTAGCCCTGAGACACTACTATCGGTTTAATTTAAGGTCGGTCAATTTGGGAGTTTCGAGAACTACGAGTACCGTACGGTTAAAGGGATCTGTTCTAATCCCGTACAAACTGATTCTCATTGTTAGGAGGAGCCTTGTCCCATCTAATAAACCGACGTCATCTTTGGAGCGACTTAGAGCCTAAAGCCGGTTCCCTGACATACGGCAGATCAAACTATGGTAACTCAAGTCGATAACTTGTTAAATCGCGGTTGATATCTGAGTAGAATTGCGCCAGAGGCCGGGGAAGTGACTTCGTCACTCCTGCACCAGGCTCCTATCTTAGCTTGCTGAGAACCGAGGTCAAAAAAGGCCTACGCAGATCGGGCCCCTGGGCACATACAATAGGCCCAGCGTCGACATACCGATCCATCCTCTGACTACCTAAGGCCGCGCTGTACGAGAACGAACTCATTATTGAATGAGCTCGGGGCTATGACTACGCGAACTTAGTAACTCCAAGAATGCGCCGCCAACGAAGATGCTTAACTTGGCGAACGAGCGTTATACGAGCCTACAAAAAAGTTTATATAGATATTAAATGGTTTCTGTCAGATCCAACGTCATTAAGTATGTGAATAATTCGTCCGCAGTCCCTGGTCTGTTGTTTGTAACAAACAACGCACGAAGTTAATCGTTAATGACACGAAGTTGCTGTGGCGTGATATGGGTTAGGGAATGGAGGCTTATTTCTGGCCGGTAAATAACCTTTATTCCTAGAAAGCATGTCTTCATACATGGAGGTCCAAGCGAGCAACCGCCGGATCTGTAAGATGTCAAACTGCTTGCCTTAAAGATATCGCGACGTATCTGTTCAAACCACTGTCCTCTCCAGACTCGGGGGTCTGG"
S2="GAGCGTTGAGGGGTGCGTTGCTTAAATCCGATCCGGTCACACTTTTTCACTAGCAATAACCTCGCGTCACCTCTGTAGAGTACTGCACAGTTCGTTCAATGGGGGGGACCCGAAATCTCCGGATATCGTGGATCGTAAAGGATCGCTTGGACTCCGGAGCAAGGATTTTCACGCTGTTAAAAAAAGACGTCGGTGAAATATAGGACTAACCCTAACCACTTAGCGACCTTGATCCTATAGGCTGTTGCCCTACTTACGGCCCTTTTATGCGAGGGCACTCTACGCGATAATATGGGTATTGGCGCGTGCAAAAACGCCAATGTTGATCCATACCTCTATGAGTTATTTGCGTTTCGACTGCCTTCTTCAATACCCACTATATGCGTACGATCTCATTCCTACACTCGCCCTACGGACTGGGCCCCCGAAGTCATTCAAGTGAACTCTAGTTGATGTTTCTATTCAATGCCATGCCCAGGACACCTGCGGGCCCGCAGACCGTCAGAGGCCGAGGCTAAACACTGTACAATCAGTTGGCTAACTAAGGAGGTCCCGATAATCGCTAACAGCGCTCATCGGTATATTACCCCCGAGGCATGGGCAGAGGCTATAACACCTTCTAGCTTGATAGAGTTTAGTATCTGCCTTCACCGAGATCATTACGTAGGCGACGTGCCTTCCAGTAGCCTTTCGACTGTTGTGTCACAATAACCACACATACGATACATGGATACGCGCCGGTGATTCCGGTGATGTCTTGGAACTTACGGAATCCATGATTATACCTGTCTTACAAATTCCCTTAGAACCTCAGATGCATTTTGTTAAACAGTAAGGACGTAGTGAGCAACCTCTGGATAGCAAGATTTGCATAGTCCTATTTTCAGATATAGAAGAAGGTGCCGAGTCAGCCCGATGCTATGTCCCCAGAAGTTGCTCTGG"

if len(S1) == len(S2):

  Hamming_Distance = 0

  for n in range(len(S1)):
    if S1[n] != S2[n]:
      Hamming_Distance += 1
  print(Hamming_Distance)
else:
  raise Exception("One sequence is too short or too long.")