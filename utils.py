import numpy as np 
import pickle
import json

class churn_prediction():
    def __init__(self,data):
        self.data = data

    def loading_files(self):

        with open(r'artifacts/project_data.json','r') as file:
            self.project_data = json.load(file)

        with open(r'artifacts/random_forest_model.pkl','rb') as file:
            self.model = pickle.load(file)

    def customer_churn(self):
        self.loading_files()

        Tenure = self.data['html_Tenure']
        PreferredLoginDevice = self.data['html_PreferredLoginDevice']
        CityTier = self.data['html_CityTier']
        WarehouseToHome = self.data['html_WarehouseToHome']
        PreferredPaymentMode = self.data['html_PreferredPaymentMode']
        Gender = self.data['html_Gender']
        HourSpendOnApp = self.data['html_HourSpendOnApp']
        NumberOfDeviceRegistered = self.data['html_NumberOfDeviceRegistered']
        SatisfactionScore = self.data['html_SatisfactionScore']
        MaritalStatus = self.data["html_MaritalStatus"]
        NumberOfAddress = self.data['html_NumberOfAddress']
        Complain = self.data['html_Complain']
        OrderAmountHikeFromlastYear = self.data['html_OrderAmountHikeFromlastYear']
        CouponUsed = self.data['html_CouponUsed']
        OrderCount = self.data['html_OrderCount']
        DaySinceLastOrder = self.data['html_DaySinceLastOrder']
        CashbackAmount = self.data['html_CashbackAmount']
        PreferedOrderCat = self.data['html_PreferedOrderCat']

        user_data = np.zeros(len(self.project_data['columns']))

        user_data[0] = Tenure
        user_data[1] = self.project_data['PreferredLoginDevice'][PreferredLoginDevice]
        user_data[2] = CityTier
        user_data[3] = WarehouseToHome
        user_data[4] = self.project_data['PreferredPaymentMode'][PreferredPaymentMode]
        user_data[5] = self.project_data['Gender'][Gender]
        user_data[6] = HourSpendOnApp
        user_data[7] = NumberOfDeviceRegistered
        user_data[8] = SatisfactionScore
        user_data[9] = self.project_data['MaritalStatus'][MaritalStatus]
        user_data[10] = NumberOfAddress
        user_data[11] = Complain
        user_data[12] = OrderAmountHikeFromlastYear
        user_data[13] = CouponUsed
        user_data[14] = OrderCount
        user_data[15] = DaySinceLastOrder
        user_data[16] = CashbackAmount


        cat = 'PreferedOrderCat_'+PreferedOrderCat
        index = np.where(self.project_data['columns'] == cat)[0]

        user_data[index] = 1

        result = self.model.predict([user_data])[0]
        
        return result

        