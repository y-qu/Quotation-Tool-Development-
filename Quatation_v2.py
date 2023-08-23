#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Leetcode 
@File    ：Quatation_v2.py
@Author  ：Yanni
@Date    ：2023/7/21 15:12 
'''

import time
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
# from tkmacosx import Button
import numpy as np
from random import sample
from tkinter import messagebox


class Quotation():

    def __init__(self):
        self.set_global_config()
        self.init(title='My Quotation')

    def init(self, title):
        window = tk.Tk()
        window.title(title)  # 设置窗口的标题
        window.geometry('800x800')
        window.resizable(0, 0)
        self.window = window
        self.main()
        self.window.mainloop()

    def set_global_config(self):
        self.audit_type_dict = {
            "ASHRAE Level 0 (Walkthrough)": 1000,
            "ASHRAE Level 1 (Benchmarking)": 2000,
            "ASHRAE Level 2": 3000,
            "ASHRAE Level 3 (Investment Grade)": 4000,
            "CEG Audit": 5000,
            "SEAI Compliance Audit (SI 599)": 6000
        }

        self.facility_type_dict = {
            'Office': 1000,
            'Dwelling': 2000,
            'Warehouse': 3000,
            'SportsSocialClub': 4000,
            'Manufacturing': 5000
        }

        self.drone_service_dict = {
            0: 0,  # 0 False
            1: 500  # 1 True
        }

        self.width_dict = {
            'text_type': 100
        }

        self.heith_dict = {}

    def do_cal(self, unitPrice=1.0,
               sizeOfArea=1.0,
               audit_type='ASHRAE Level 0 (Walkthrough)',
               facility_type='Office',
               drone_service_fees=500,
               drone_service_code=0
               ):

        cost = unitPrice * sizeOfArea + self.audit_type_dict[audit_type] + self.facility_type_dict[facility_type]+drone_service_fees*drone_service_code



        return cost

    def summit_button_click(self):
        print("do calculate !")

        try:

            audit_combo_select = self.audio_type_tk_combo.get()
            facility_combo_select = self.facility_type_tk_combo.get()

            print("audit_combo_select:{}; facility_combo_select:{}".format(audit_combo_select, facility_combo_select))

            unitPrice = float(self.unit_price_tk_entry.get())
            sizeOfArea = float(self.sizeOfArea_tk_entry.get())
            print("unitPrice:{}; sizeOfArea:{}".format(unitPrice, sizeOfArea))

            drone_fees = float(self.drone_fee_tk_entry.get())
            drone_radio_value = int(self.drone_tk_radioValue.get())
            print("drone_fees:{}; drone_radio_value: {}".format(drone_fees,drone_radio_value))

        except:
            self.show_error_message()


        total_cost = self.do_cal(unitPrice=unitPrice,
                                 sizeOfArea=sizeOfArea,
                                 audit_type=audit_combo_select,
                                 facility_type=facility_combo_select,
                                 drone_service_fees=drone_fees,
                                 drone_service_code=drone_radio_value)

        self.total_cost_tk_label['text'] = 'Total cost:   {}'.format(total_cost)

    def radio_select(self, ):
        pass

    def combo_call_back(self, event):
        print(self.audio_type_tk_combo.current(), self.audio_type_tk_combo.get())
        print('111', event)

    def first_line(self):
        self.audio_type_tk_label = tk.Label(self.window, text='Audit Type: ', font=("Times", 20), anchor='nw')
        self.audio_type_tk_label.place(x=50, y=50, width=120, height=80, anchor='nw')

        self.audio_type_tk_combo = ttk.Combobox(self.window,
                                                values=list(self.audit_type_dict.keys()))

        self.audio_type_tk_combo.place(x=180, y=50, width=300, height=40, anchor='nw')

        self.audio_type_tk_combo.current(0)  # default value

        # self.audio_type_tk_combo.bind("<<ComboboxSelected>>", self.combo_call_back)

    def second_line(self):
        self.facility_type_tk_label = tk.Label(self.window, text='Facility Type: ', font=("Times", 20), anchor='nw')
        self.facility_type_tk_label.place(x=50, y=150, width=120, height=80, anchor='nw')

        self.facility_type_tk_combo = ttk.Combobox(self.window,
                                                   values=list(self.facility_type_dict.keys()))

        self.facility_type_tk_combo.place(x=180, y=150, width=300, height=40, anchor='nw')

        self.facility_type_tk_combo.current(0)  # default value

    def third_line(self):
        self.unit_price_tk_label = tk.Label(self.window, text='UnitPrice: ', font=("Times", 20), anchor='nw')
        self.unit_price_tk_label.place(x=50, y=250, width=120, height=90, anchor='nw')

        self.unit_price_tk_entry = tk.Entry(self.window, )
        self.unit_price_tk_entry.place(x=180, y=250, width=200, height=30, anchor='nw')

    def four_line(self):
        self.sizeOfArea_tk_label = tk.Label(self.window, text='SizeOfArea: ', font=("Times", 20), anchor='nw')
        self.sizeOfArea_tk_label.place(x=50, y=350, width=120, height=80, anchor='nw')

        self.sizeOfArea_tk_entry = tk.Entry(self.window, )
        self.sizeOfArea_tk_entry.place(x=180, y=350, width=200, height=30, anchor='nw')

    def five_line(self):
        self.drone_fee_tk_label = tk.Label(self.window, text='Drone Fees: ', font=("Times", 20), anchor='nw')
        self.drone_fee_tk_label.place(x=50, y=450, width=120, height=80, anchor='nw')

        self.drone_fee_tk_entry = tk.Entry(self.window, )
        self.drone_fee_tk_entry.place(x=180, y=450, width=200, height=30, anchor='nw')

        self.drone_tk_radioValue = tk.IntVar()

        self.drone_tk_yes = tk.Radiobutton(self.window, text='Yes',
                                           variable=self.drone_tk_radioValue, value=1)
        self.drone_tk_yes.place(x=180, y=500, width=60, height=30, anchor='nw')

        self.drone_tk_no = tk.Radiobutton(self.window, text='No',
                                          variable=self.drone_tk_radioValue, value=0)
        self.drone_tk_no.place(x=180 + 70, y=500, width=60, height=30, anchor='nw')

    def six_line(self):
        self.summit_tk_button = tk.Button(self.window,
                                          text='Calculate',  # 显示在按钮上的文字
                                          font=("Times", 20),
                                          command=self.summit_button_click,
                                          anchor='center')

        self.summit_tk_button.place(x=100, y=600, width=600, height=50, anchor='nw')

    def seven_line(self):
        self.total_cost_tk_label = tk.Label(self.window, text='Total cost: ', font=("Times", 25), anchor='nw')
        self.total_cost_tk_label.place(x=50, y=700, width=600, height=30, anchor='nw')

    def show_error_message(self):
        messagebox.showinfo('Error', 'All params should be required！')
    def main(self):


        self.first_line()
        self.second_line()
        self.third_line()
        self.four_line()

        self.five_line()
        self.six_line()
        self.seven_line()


quotation_obj = Quotation()
quotation_obj.main()
