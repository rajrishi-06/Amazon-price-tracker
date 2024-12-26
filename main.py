import time
from amazon import Amazon
from notification_manager import NotificationManager

notifier = NotificationManager()
website = input("Enter the product url: ")
target_price = int(input("What is your target price on the product: "))
email = input("Enter the email to get notified: ")
product = Amazon(website,target_price)
outcome = product.check_product()
diff = target_price - product.current_price
if outcome:
    notifier.send_email(message_body=f"Subject:{product.product_name} Price Alert!!!"
                                     f"\n\nThe product price is now Rs.{product.current_price},"
                                     f"below your target price with a difference of Rs.{diff}"
                                     f"\nBUY NOW!!!",to_email=email)
    print("Target Price reached, email sent successfully.")
else:
    print(f"Target price not reached,there is a difference of Rs.{-diff} .Check Tomorrow")