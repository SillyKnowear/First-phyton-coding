def display_invoice(username, amount, due_date):
    print(f'Invoice for {username}')
    print(f'Amount: ${amount:.2f} is due: {due_date}')

display_invoice('johndoe', 150.75, '2024-07-15')