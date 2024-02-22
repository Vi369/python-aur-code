#Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

# ordered_Size = "medium"
ordered_Size = "large"
extra_shot = True if ordered_Size == 'large' else False

if extra_shot:
    coffee = ordered_Size + " Coffee with in a extra shot"
else:
    coffee = ordered_Size + " Coffee"
print("order:", coffee)