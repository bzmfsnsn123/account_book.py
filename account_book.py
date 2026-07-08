from datetime import date
FILE="account.txt"
def load_account():
    bills=[]
    try:
        with open(FILE,"r",encoding="utf-8") as f:
             for line in f:
                 line = line.strip()
                 if not line:
                    continue
                 bills_date,typ,amount,remark = line.split()
                 bills.append({
                "date":bills_date,
                "type":typ,
                "amount":amount,
                "remark":remark,
            })

    except FileNotFoundError:
        pass
    return bills
def save_account(bills):
    with open(FILE,"w",encoding="utf-8") as f:
        for b in bills:
            f.write(f"{b['date']}|{b['type']}|{b['amount']}|{b['remark']}\n")

def main():
    bill_list = load_account()
    while True:
        print("\n======简易收支记账本======")
        print("1.记录一笔收入")
        print("2.记录一笔支出")
        print("3.查看全部账单")
        print("4.统计收支总览")
        print("5.删除指定记录")
        print("6.删除所有账单")
        print("0.退出程序")
        try:
            opt=int(input("请输入功能序号："))
            if opt == 1 or opt==2:
                date_input=input("请输入日期（如：2026-07-08 输入空格直接默认本地时间）：")
                if date_input=="":
                    date_input=date.today().strftime("%Y-%m-%d")
                amount_str=input("输入金额：").strip()
                try:
                    amount=float(amount_str)
                    if amount <= 0:
                        print("金额必须大于0")
                        continue

                except ValueError:
                    print("请输入合法数字")
                    continue
                remark=input("输入备注：").strip()
                typ="收入" if opt==1 else "支出"
                bill_list.append({
                    "date":date_input,
                    "type":typ,
                    "amount":amount,
                    "remark":remark,
                })
                save_account(bill_list)
                print(f"{typ}记录添加成功！")

            elif opt==5:
                if not bill_list:
                    print("暂无账单记录")
                    continue
                idx_str=input("输入要删除的记录序号").strip()
                try:
                    idx=int(idx_str)
                    if idx < 0 or idx >= len(bill_list):
                        print("序号超过范围！")
                        continue
                except ValueError:
                    print("请输入有效数字！")
                    continue
                del bill_list[idx-1]
                save_account(bill_list)
                print("记录已删除")

            elif opt == 3:
                 if not bill_list:
                    print("暂无账单记录")
                    continue
                 print(f"\n{'序号':<4}{'日期':<12}{'类型':<6}{'金额':<8}{'备注'}")
                 print("-" * 40)
                 for i, b in enumerate(bill_list, 1):
                    print(f"{i:<4}{b['date']:<12}{b['type']:<6}{b['amount']:<8}{b['remark']}")

            elif opt == 4:
                if not bill_list:
                  print("暂无数据，无法统计")
                  continue
                income = sum(b["amount"] for b in bill_list if b["type"] == "收入")
                expense = sum(b["amount"] for b in bill_list if b["type"] == "支出")
                balance = income - expense
                print(f"\n===== 收支总览 =====")
                print(f"总收入：{income:.2f} 元")
                print(f"总支出：{expense:.2f} 元")
                print(f"当前结余：{balance:.2f} 元")

            elif opt == 6:
                confirm=input("确定清空所有账单吗?(y/n)")
                if confirm == "y":
                    bill_list.clear()
                    save_account(bill_list)
                    print("所有账单已清空")
                else:
                    print("已取消操作")

            elif opt ==0:
                print("程序退出，账单已保存")
                break
            else:
                print("请输入0-6之间的数字")
        except ValueError:
            print("输入错误，请输入有效数字")
if __name__=="__main__":
    main()








