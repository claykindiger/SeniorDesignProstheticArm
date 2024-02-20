import pandas as pd

res1 = pd.read_csv('experiment_results_1ft.csv')
res15 = pd.read_csv('experiment_results_1.5 ft.csv')
res2 = pd.read_csv('experiment_results_2ft.csv')
res3 = pd.read_csv('experiment_results_3ft.csv')

res1['distance'] = '1ft'

results = pd.concat([res1,res15,res2,res3],ignore_index=True)

results['runtime'] = results['runtime'].apply(lambda x: float(x.split(':')[-1].split(' ')[0]))

res_gb_distance = []

for dist, group in results.groupby('distance'):
	res = {}
	res['distance'] = dist
	res['num_trials'] = group.shape[0]
	res['average_runtime'] = group['runtime'].mean()
	corr_lab = group[group['predicted_label'] == group['correct_label']].shape[0]
	res['accuracy'] = corr_lab / group.shape[0]
	res_gb_distance.append(res)

res_gb_distance = pd.DataFrame(res_gb_distance)

results.to_csv('full_experiment_results.csv')
res_gb_distance.to_csv('summarized_experiment_results.csv')
