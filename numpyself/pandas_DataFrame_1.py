import pandas as pd
# region
dic = {
    'Name': ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff'],
    'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Female'],
    'Class': ['CS_101', 'CS_102', 'CS_101', 'CS_102', 'CS_101', 'CS_102'],
    'Chi': [80, 100, 60, 80, 80, 80],
    'Eng': [80, 80, 50, 70, 80, 80],
    'Math': [50, 100, 75, 85, 50, 80]
}

scores_df = pd.DataFrame(dic,
                         columns=['Name', 'Gender',
                                  'Class', 'Chi', 'Eng', 'Math'],
                         index=list('abcdef'))
# print(scores_df)
# print(scores_df.ndim)
# print(scores_df.shape)
# print(scores_df.values)
# print(scores_df.index)

# print(scores_df.describe())
# print(scores_df.info())
# print(scores_df.head(3))
# print(scores_df.tail(3))
# scores_df.to_csv('data/scores.csv')
# scores_df.to_excel('data/scores.xlsx')
# endregion
# region
scores = pd.read_excel('data/scores.xlsx')
print(scores)
scores_chi = scores.Chi
print(scores_chi)
print(scores_chi.sum())
# print(scores_df['Chi'])
# print(scores_df.Chi.sum())
# scores_df = scores_df.Name.apply(str.upper)

print(scores.loc['a':'c', 'Chi':'Math'])


print(scores.loc['a':'c', 'Chi':'Math'])
print(scores.loc['a':'c', ['Chi', 'Eng']])
print(scores.loc[scores.Eng > 60, ['Class', 'Name', 'Eng']])
print(scores[scores > 60])
print(scores[scores < 60])
# endregion
