"""
Currency Converter / 通貨コンバーター
=====================================
A simple terminal-based currency converter supporting USD, BDT, and JPY.
USD・BDT・JPY間で通貨を変換するシンプルなターミナルアプリです。

Author: Hossain Sarwar
"""

class Converter:
    
    # ── Constants ──────────────────────────────────────────────────────────────────
    def currency_rate(self) -> dict[str, int]:
        rates: dict[str, int] = {
            "USD" : 1,
            "BDT" : 120,
            "JPY" : 150
        }
        return rates
    
    # ── Helper functions ───────────────────────────────────────────────────────────
    
    def user_input(self) -> tuple[str, str, int]:
        """
        Get currency selection and amount from the user.
        通貨の選択と金額をユーザーから取得します。
        
        Returns:
            tuple: (current_curr, convert_curr, current_amount)
                   (変換元通貨, 変換先通貨, 金額)
        """
        # Get currency selection from user / 通貨を選択させる
        current_curr, convert_curr = self.get_currency()
        
        # Get amount from user / 金額を入力させる
        while True:
            try:
                current_amount = int(input("\n    Input the amount. / 金額をお入れください。: --> "))  #check input is not <0
            except ValueError:
                # Handle non-numeric input / 数字以外の入力を処理
                print("    ⚠ Invalid input. Please enter a number. / 数字を入力してください。")
                continue
            if current_amount < 0 :
                # Reject negative amounts / マイナスの金額を拒否
                print("    ⚠ Negative amount not supported. / マイナスの金額は使用できません。")
                continue
            break              
        return current_curr, convert_curr, current_amount
    
    def format_amount(self,currency: str, amount: int|float,logo: str) -> str:
        """Return a formatted string with the currency symbol in the correct position.
        通貨記号を正しい位置に配置したフォーマット済み文字列を返します。
        """       
        if logo in ["$","¥"]:
            return f"    {currency}: {logo}{amount}"
        else:
            return f"    {currency}: {amount} {logo}"
               
    def last_view(self) -> None:
        """
        Display a farewell message and exit the program.
        終了メッセージを表示してプログラムを終了します。
        """
        print("\n    Thank you for using Currency Converter! \n"
              "        ご利用ありがとうございました！")
    
    # ── Currency selection ─────────────────────────────────────────────────────
    
    def get_currency(self, 
                     current_curr: str | None = None,
                     convert_curr: str | None = None, 
                     current_curr_flag: bool = True,
                     convert_curr_flag: bool = True) -> tuple[str, str]:
        
        """Display the currency menu and return the selected currency code.
        通貨メニューを表示し、選択された通貨コードを返します。
        
        Args:
            current_curr (str): Previously selected source currency / 変換元通貨
            convert_curr (str): Previously selected target currency / 変換先通貨
            current_curr_flag (bool): If True, ask user to select source currency
                                      Trueの場合、変換元通貨を選択させる
            convert_curr_flag (bool): If True, ask user to select target currency
                                      Trueの場合、変換先通貨を選択させる
        Returns:
            tuple: (current_curr, convert_curr) / (変換元通貨, 変換先通貨)
        """
        # Build currency list from rates / レートから通貨リストを作成
        rates= self.currency_rate()
        currencyList =[]
        for key in rates.keys():
            currencyList.append(key)
            
        # Select source currency if flag is True / フラグがTrueの場合、変換元通貨を選択
        if current_curr_flag == True  :  
            while True:
                try:
                    current_curr = int(input("\n    Choose current currency. / 変換元の通貨を選んでください。: \n"
                        "      1. USD \n"
                        "      2. BDT \n"
                        "      3. JPY \n"
                        "         --> "))
                except ValueError:
                    # Handle non-numeric input / 数字以外の入力を処理
                    print("    ⚠ Invalid input. Please enter a number. / 数字を入力してください。")
                    continue
                if 1 > current_curr  or current_curr >3:
                    print("    ⚠ Invalid number. / 正しい番号をお入れください。")
                    continue
                else:
                    # Convert number to currency code / 数字を通貨コードに変換
                    current_curr = currencyList[current_curr - 1]
                    break
        
         # Select target currency if flag is True / フラグがTrueの場合、変換先通貨を選択       
        if convert_curr_flag == True  : 
            # Remove selected source currency from list / 選択済みの変換元通貨をリストから削除
            if current_curr in currencyList:
                currencyList.remove(current_curr)
            print(f"\n    Choose convert currency. / 変換先の通貨を選んでください。: ")
            for i,key in enumerate(currencyList):
                print(f"      {i+1}. {key} ")         
            while True:
                try:
                    convert_curr = int (input("         --> "))
                except ValueError:
                    # Handle non-numeric input / 数字以外の入力を処理
                    print("    ⚠ Invalid input. Please enter a number. / 数字を入力してください。")
                    continue
                if 1 > convert_curr  or convert_curr >2:
                    print("    ⚠ Invalid number. / 正しい番号をお入れください。")
                    continue
                else:
                    # Convert number to currency code / 数字を通貨コードに変換
                    convert_curr = currencyList[convert_curr - 1]
                    break
        return current_curr, convert_curr
    
    # ── Display ────────────────────────────────────────────────────────────────
          
    def output(self, current_curr: str, convert_curr: str, current_amount: int) -> float:
        """
        Calculate the converted currency amount via USD as base currency.
        USD を基準通貨として変換後の金額を計算します。
        Args:
            current_curr (str): Source currency code / 変換元の通貨コード
            convert_curr (str): Target currency code / 変換先の通貨コード
            current_amount (int): Amount to convert / 変換する金額
        Returns:
            float: Converted amount / 変換後の金額
        """
        rates = self.currency_rate()
        USD_amount = current_amount / rates[current_curr]
        convert_amount = USD_amount * rates[convert_curr]
        return convert_amount
    
    def result(self,
               current_curr  : str,
               convert_curr  : str,
               current_amount: int,
               convert_amount: float
               ) -> None:
        """
        Display the conversion result with currency symbols.
        通貨記号付きで変換結果を表示します。
        Args:
            current_curr (str): Source currency code / 変換元の通貨コード
            convert_curr (str): Target currency code / 変換先の通貨コード
            current_amount (int): Original amount / 変換前の金額
            convert_amount (float): Converted amount / 変換後の金額
        """
        current_curr_logo = ("$"if current_curr == "USD"
                            else "¥" if current_curr == "JPY" else "Tk" )
        convert_curr_logo = ("$"if convert_curr == "USD" 
                            else "¥" if convert_curr == "JPY" else "Tk")
        print(f"\n    == Result / 結果 ==")
        print(self.format_amount(current_curr, current_amount, current_curr_logo))
        print(f"    [Converted amount | 変換先] "
              f"{self.format_amount(convert_curr, convert_amount, convert_curr_logo)}")
        print(f"{'-'*60} \n")
        
    # ── Confirmation loop ──────────────────────────────────────────────────────
    
    def confirmation(self, 
                     current_curr   : str, 
                     convert_curr   : str, 
                     current_amount : int) -> tuple[str, str, int] | None:
        """
        Ask the user whether to change amount or currency, then update accordingly.
        金額または通貨を変更するか確認し、必要に応じて更新します。
        Args:
            current_curr (str): Source currency code / 変換元の通貨コード
            convert_curr (str): Target currency code / 変換先の通貨コード
            current_amount (int): Current amount / 現在の金額
        Returns:
            tuple: Updated (current_curr, convert_curr, current_amount)
                   更新された (変換元通貨, 変換先通貨, 金額)
            None: If user wants to restart / 最初からやり直す場合はNone
        """
        while True:
            changed = False # Track if anything has changed / 変更があったかどうかを追跡
            # ── Amount change / 金額の変更 ────────────────────────────────
            amount_again =input("    Do you want to change the amount? / 金額を変更しますか？ (y/n): --> ")
            if amount_again.lower() == "y":
                while True:
                    try:
                        current_amount = int(input("\n    Input the amount. / 金額をお入れください。: --> "))  #check input is not <0
                    except ValueError:
                        print("    ⚠ Invalid input. Please enter a number. / 数字を入力してください。")
                        continue
                    if current_amount < 0 :
                        print("    ⚠ Negative amount is not supported. / マイナスの金額は使用できません。")
                        continue
                    break
                changed = True
                    
            elif amount_again.lower() == "n":
                pass 
            else:
                print("    ⚠ Please enter y or n. / y か n を入力してください。")
                continue
         
            # ── Currency change / 通貨の変更 ──────────────────────────────
            while True:
                currency_again = input("    Do you want to change currency? / 通貨を変更しますか？ (y/n): --> ")
                if currency_again.lower() == "y":
                    while True:
                        try:
                            select_currency = int(input("\n    Choose your currency. / 通貨を選択してください。\n"
                                                        "    1. Current currency / 変換元\n"
                                                        "    2. Convert currency / 変換先 \n"
                                                        "    3. Both / 両方\n"
                                                        "       --> "))
                        except ValueError:
                            print("    ⚠ Invalid input. / 正しい番号をお入れください。")
                            continue
                        if select_currency not in [1,2,3]:
                            print("    ⚠ Invalid number. / 正しい番号をお入れください。")
                            continue
                        break
                    # Change source currency only / 変換元通貨のみ変更
                    if select_currency == 1 :
                        current_curr_flag = True
                        convert_curr_flag = False
                        
                        current_curr, convert_curr = self.get_currency(current_curr, convert_curr, 
                                                                   current_curr_flag, convert_curr_flag)
                    # Change target currency only / 変換先通貨のみ変更
                    elif select_currency == 2:
                        current_curr_flag = False
                        convert_curr_flag = True
                        current_curr, convert_curr = self.get_currency(current_curr, convert_curr,
                                                                    current_curr_flag, convert_curr_flag)      
                    # Change both currencies / 両方の通貨を変更
                    else:
                        current_curr_flag = True
                        convert_curr_flag = True
                        current_curr, convert_curr = self.get_currency(current_curr, convert_curr, 
                                                                    current_curr_flag, convert_curr_flag)
                    changed = True  
                    return  current_curr, convert_curr, current_amount
                    

                elif currency_again.lower() == "n":
                    if changed == True: # 何かの変更があった場合
                        # Show new result with updated amount / 更新された金額で新しい結果を表示
                        convert_amount = self.output(current_curr, convert_curr, current_amount)
                        self.result(current_curr, convert_curr, current_amount, convert_amount)
                        break
                    else:
                    # Nothing changed → ask to finish or restart
                    # 変更なし → 終了または最初からやり直すか確認
                        while True:
                            close =input("    Are you sure to finish? / 終了しますか？ (y/n): --> ")
                            if close.lower() =="y":
                                self.last_view()  #show farewell message / 最終のメッセージを表示
                                exit() # Exit the program / プログラムを終了
                                break
                            elif close.lower() == "n":
                                # Restart from the beginning / 最初からやり直す
                                return None
 
                            else:
                                print("    ⚠ Please enter y or n. / y か n を入力してください。")
                                continue
                else:
                    print("    ⚠ Please enter y or n. / y か n を入力してください。")
                    continue
                

    # ── Entry point ────────────────────────────────────────────────────────────
           
    def loop(self) -> None:
        """
        Main loop of the application. Controls the overall program flow.
        アプリケーションのメインループ。プログラム全体の流れを制御します。
        """
        # Display title / タイトルを表示
        border = "-"*49
        title = "|  === Currency Converter / 通貨コンバーター ===  |"
        print(f"\n{border.center(68)}\n{title.center(60)}\n{border.center(68)}")
        
        # Outer loop: restart from beginning if user chooses to
        # 外側のループ: ユーザーが選択した場合、最初からやり直す
        while True:
            # Get initial currency and amount from user
            # ユーザーから通貨と金額を取得
            current_curr, convert_curr, current_amount = self.user_input()
            
            # Inner loop: show result and handle changes
            # 内側のループ: 結果を表示し、変更を処理する
            while True:
                # Calculate and display result / 結果を計算して表示
                convert_amount = self.output(current_curr, convert_curr, current_amount)
                self.result(current_curr, convert_curr, current_amount, convert_amount)
                # Ask user for changes / ユーザーに変更を確認
                result = self.confirmation(current_curr, convert_curr, current_amount)
                # None means restart from beginning / Noneは最初からやり直すことを意味する
                if result is None:
                    break
                # Update values with user's changes / ユーザーの変更で値を更新
                current_curr, convert_curr, current_amount = result

# ── Run ────────────────────────────────────────────────────────────────────────
               
if __name__ == "__main__":
    Converter().loop()
            