import common as co
import user_recommendation_system as us
import item_recommedation_system as it

r = [
    [1,1,1],
    [2,2,2],
    [0,0,4],
    ]

print("Mean of a row: {}".format(co.mean_row(r[0])))
print()
user_items = [
                [5,3,4,4,None],
                [3,1,2,3,3],
                [4,3,4,3,5],
                [3,3,1,5,4],
                [1,5,5,2,1]
    ]
threshold = 0.0
print("Pearson's users simility index: {}".format(us.sim_user(user_items[0],user_items[1])))
print("Optimization of users predition : {}".format(us.optimization_pred_user(0,user_items,threshold)))
print("Valoration  of user preditions: {}".format(us.pred_user(0,4,user_items,threshold)))
print()


t_user_items = it.transpuesta(user_items)

print("Pearson's items simility index: {}".format(it.sim_item(t_user_items[:][0],t_user_items[:][len(t_user_items)-1])))
print("Optimization of items predition: {}".format(it.optimization_pred_item(0,t_user_items,threshold)))
print("Valoration  of items preditions: {}".format(it.pred_item(0,len(t_user_items)-1,t_user_items,threshold)))

