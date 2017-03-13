import common as co
import item_recommedation_system as it
import shopping_basket_recommendation_system as sh
import user_recommendation_system as us

r = [
    [1, 1, 1],
    [2, 2, 2],
    [0, 0, 4],
]

print("Mean of a row: {}".format(co.mean_row(r[0])))
print()

user_items = [
    [5, 3, 4, 4, None],
    [3, 1, 2, 3, 3],
    [4, 3, 4, 3, 5],
    [3, 3, 1, 5, 4],
    [1, 5, 5, 2, 1]
]
threshold = 0.0
print("Pearson's users similarity index: {}".format(us.sim_user(user_items[0], user_items[1])))
print("Optimization of users prediction : {}".format(us.optimization_prediction_user(0, user_items, threshold)))
print("Validation of user predictions: {}".format(us.prediction_user(0, 4, user_items, threshold)))
print()

t_user_items = it.transpose(user_items)
print("Pearson's items similarity index: {}".format(
    it.sim_item(t_user_items[:][0], t_user_items[:][len(t_user_items) - 1])))
print("Optimization of items prediction: {}".format(it.optimization_prediction_item(0, t_user_items, threshold)))
print("Validation of items predictions: {}".format(it.prediction_item(0, len(t_user_items) - 1,
                                                                      t_user_items, threshold)))
print()

print("Wait for the operations:")
directory = "./data_files/"
file1 = "u.data"
threshold = -1.0
limits_elements_reads = 10
user_items = co.read_data_file_with_recommendation(directory + file1, limits_elements_reads)
print("Pearson's users similarity index: {}".format(us.sim_user(user_items[0], user_items[1])))
print("Optimization of users prediction : {}".format(us.optimization_prediction_user(0, user_items, threshold)))
print("Validation of user predictions: {}".format(us.prediction_user(0, 4, user_items, threshold)))
print()

t_user_items = it.transpose(user_items)

print("Pearson's items similarity index: {}".format(it.sim_item(t_user_items[0], t_user_items[len(t_user_items) - 1])))
print("Optimization of items prediction: {}".format(it.optimization_prediction_item(0, t_user_items, threshold)))
print("Validation of items predictions: {}".format(it.prediction_item(0, len(t_user_items) - 1,
                                                                      t_user_items, threshold)))
print()
limits_elements_reads = 4
support_min = 2
confidence_min = 1
file2 = "retail.dat"

t = ['1 3 4', '2 3 5', '1 2 3 5', '2 5']
print("Apriori algorithm {}".format(sh.apriori_algorithm(directory, file2,
                                                         limits_elements_reads, support_min, confidence_min, t)))
print()

t = None
print("Apriori algorithm {}".format(sh.apriori_algorithm(directory, file2,
                                                         limits_elements_reads, support_min, confidence_min, t)))
