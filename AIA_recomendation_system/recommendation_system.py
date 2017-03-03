import user_recommendation_system as us
import item_recommedation_system as it
#means test
r = [
    [1,1,1],
    [2,2,2],
    [0,0,4],
    ]

#print(us.mean_row(r[0]))
#print(it.mean_col(r,2))

user_items = [
                [5,3,4,4,None],
                [3,1,2,3,3],
                [4,3,4,3,5],
                [3,3,1,5,4],
                [1,5,5,2,1]
    ]
#print(us.sim_user(user_items[0],user_items[1]))
#print(us.optimization_pred_user(0,user_items,0.0))
#print(us.pred_user(0,4,user_items))



t_user_items = it.transpuesta(user_items)

print(it.sim_item(t_user_items[:][0],t_user_items[:][len(t_user_items)-1]))



