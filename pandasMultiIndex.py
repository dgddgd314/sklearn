
arr = [[10,10,10,30,30,30],
       ['red','green','blue','red','green','blue']]

m_idx = pd.MultiIndex.from_arrays(arr)
print(m_idx)

ar = [['S','S','S','K','K','K','I','I','I','B','B','B'],
      [2020,2021,2022,2020,2021,2022,2020,2021,2022,2020,2021,2022]]

m_idx = pd.MultiIndex.from_arrays(ar, names = ['도시', '년도'])
print(m_idx)

city = ['S','K','I','B']
yr = [2020,2021,2022]
m_idx = pd.MultiIndex.from_product([city, yr], names = ['city','year'])   # everything!
print(m_idx)
