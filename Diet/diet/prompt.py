
# """
# Install an additional SDK for JSON schema support Google AI Python SDK

# $ pip install google.ai.generativelanguage
# """
# def get_nutrition_plan(age, gender, height, weight, preference, allergy, activity_level, goal):
#     import json
#     import google.generativeai as genai
#     from google.ai.generativelanguage_v1beta.types import content
#     prompt = f"أنشئ خطة غذائية لمدة 7 أيام لشاب يبلغ من العمر {age} عاما، وزنه {weight} كغم وطوله {height} سم. هو {activity_level} ويريد {goal}. يفضل {preference} ولديه حساسية من {allergy}. يجب أن تحتوي كل وجبة على 400-500 سعرة حرارية ويجب أن تشمل البروتين العالي، الدهون المعتدلة، والكربوهيدرات المنخفضة. يجب تقسيم الوجبات إلى الإفطار والغداء والعشاء مع وجبتين خفيفتين يومياً. يرجى تقديم أحجام الوجبات لكل وجبة والتنوع في الوجبات."
#     genai.configure(api_key="AIzaSyAZkHVWPbElqVdwXxbXtxN0q2rW8eqn_QI")
#     generation_config = {
#       "temperature": 1,
#       "top_p": 0.95,
#       "top_k": 40,
#       "max_output_tokens": 8192,
#       "response_schema": content.Schema(
#         type = content.Type.OBJECT,
#         description = "خطة غذائية بسيطة ومتوازنة وصحية ومتنوعة تتلائم مع صفات المستخدم وتفضيلاته ومقسمة إلى وجبات إفطار وغداء وعشاء مع وجبتين خفيفتين يومياً مع تقديم أحجام الوجبات وقيمها الغذائية.",
#         enum = [],
#         required = ["plan"],
#         properties = {
#           "plan": content.Schema(
#             type = content.Type.ARRAY,
#             items = content.Schema(
#               type = content.Type.OBJECT,
#               enum = [],
#               required = ["day", "notes"],
#               properties = {
#                 "day": content.Schema(
#                   type = content.Type.ARRAY,
#                   items = content.Schema(
#                     type = content.Type.OBJECT,
#                     enum = [],
#                     required = ["day_num", "meal"],
#                     properties = {
#                       "day_num": content.Schema(
#                         type = content.Type.INTEGER,
#                       ),
#                       "meal": content.Schema(
#                         type = content.Type.ARRAY,
#                         items = content.Schema(
#                           type = content.Type.OBJECT,
#                           enum = [],
#                           required = ["name", "ingredients", "calorie", "protein", "carb", "fat", "notes"],
#                           properties = {
#                             "name": content.Schema(
#                               type = content.Type.STRING,
#                             ),
#                             "ingredients": content.Schema(
#                               type = content.Type.STRING,
#                             ),
#                             "calorie": content.Schema(
#                               type = content.Type.INTEGER,
#                             ),
#                             "protein": content.Schema(
#                               type = content.Type.INTEGER,
#                             ),
#                             "carb": content.Schema(
#                               type = content.Type.INTEGER,
#                             ),
#                             "fat": content.Schema(
#                               type = content.Type.INTEGER,
#                             ),
#                             "notes": content.Schema(
#                               type = content.Type.STRING,
#                             ),
#                           },
#                         ),
#                       ),
#                     },
#                   ),
#                 ),
#                 "notes": content.Schema(
#                   type = content.Type.STRING,
#                 ),
#               },
#             ),
#           ),
#         },
#       ),
#       "response_mime_type": "application/json",
#     }

#     model = genai.GenerativeModel(
#       model_name="gemini-2.0-flash",
#       generation_config=generation_config,
#     )

#     chat_session = model.start_chat()

#     response = chat_session.send_message(prompt)

#     return json.loads(response.text)
# # print(get_nutrition_plan(45, 1, 175, 85, " المطبخ الأردني", "الفستق والفول", "غير نشيط", "انقاص الوزن"))




# def get_nutrition_plan(age, gender, height, weight, preference, allergy, activity_level, goal):
#     import json
#     import google.generativeai as genai
#     from google.ai.generativelanguage_v1beta.types import content

#     prompt = f"أنشئ خطة غذائية لمدة 7 أيام لشاب يبلغ من العمر {age} عاما، وزنه {weight} كغم وطوله {height} سم. هو {activity_level} ويريد {goal}. يفضل {preference} ولديه حساسية من {allergy}. يجب أن تحتوي كل وجبة على 400-500 سعرة حرارية ويجب أن تشمل البروتين العالي، الدهون المعتدلة، والكربوهيدرات المنخفضة. يجب تقسيم الوجبات إلى الإفطار والغداء والعشاء مع وجبتين خفيفتين يومياً. يرجى تقديم أحجام الوجبات لكل وجبة والتنوع في الوجبات."

#     genai.configure(api_key="AIzaSyAZkHVWPbElqVdwXxbXtxN0q2rW8eqn_QI")

#     generation_config = {
#         "temperature": 1,
#         "top_p": 0.95,
#         "top_k": 40,
#         "max_output_tokens": 8192,
#         "response_schema": content.Schema(
#             type=content.Type.OBJECT,
#             description="خطة غذائية بسيطة ومتوازنة وصحية ومتنوعة تتلائم مع صفات المستخدم وتفضيلاته ومقسمة إلى وجبات إفطار وغداء وعشاء مع وجبتين خفيفتين يومياً مع تقديم أحجام الوجبات وقيمها الغذائية.",
#             enum=[],
#             required=["plan"],
#             properties={
#                 "plan": content.Schema(
#                     type=content.Type.ARRAY,
#                     items=content.Schema(
#                         type=content.Type.OBJECT,
#                         enum=[],
#                         required=["day", "notes"],
#                         properties={
#                             "day": content.Schema(
#                                 type=content.Type.ARRAY,
#                                 items=content.Schema(
#                                     type=content.Type.OBJECT,
#                                     enum=[],
#                                     required=["day_num", "meal"],
#                                     properties={
#                                         "day_num": content.Schema(
#                                             type=content.Type.INTEGER,
#                                         ),
#                                         "meal": content.Schema(
#                                             type=content.Type.ARRAY,
#                                             items=content.Schema(
#                                                 type=content.Type.OBJECT,
#                                                 enum=[],
#                                                 required=["name", "ingredients", "calorie", "protein", "carb", "fat", "notes"],
#                                                 properties={
#                                                     "name": content.Schema(
#                                                         type=content.Type.STRING,
#                                                     ),
#                                                     "ingredients": content.Schema(
#                                                         type=content.Type.STRING,
#                                                     ),
#                                                     "calorie": content.Schema(
#                                                         type=content.Type.INTEGER,
#                                                     ),
#                                                     "protein": content.Schema(
#                                                         type=content.Type.INTEGER,
#                                                     ),
#                                                     "carb": content.Schema(
#                                                         type=content.Type.INTEGER,
#                                                     ),
#                                                     "fat": content.Schema(
#                                                         type=content.Type.INTEGER,
#                                                     ),
#                                                     "notes": content.Schema(
#                                                         type=content.Type.STRING,
#                                                     ),
#                                                 },
#                                             ),
#                                         ),
#                                     },
#                                 ),
#                             ),
#                             "notes": content.Schema(
#                                 type=content.Type.STRING,
#                             ),
#                         },
#                     ),
#                 ),
#             },
#         ),
#         "response_mime_type": "application/json",
#     }

#     model = genai.GenerativeModel(
#         model_name="gemini-2.0-flash",
#         generation_config=generation_config,
#     )

#     chat_session = model.start_chat()
#     response = chat_session.send_message(prompt)

#     # تحويل الناتج إلى هيكل أكثر ملاءمة للقوالب
#     data = json.loads(response.text)
#     simplified_plan = []

#     for day in data['plan']:
#         simplified_day = {
#             'day_num': day['day'][0]['day_num'],
#             'notes': day['notes'],
#             'meals': []
#         }
#         for meal in day['day'][0]['meal']:
#             simplified_meal = {
#                 'name': meal['name'],
#                 'ingredients': meal['ingredients'],
#                 'calorie': meal['calorie'],
#                 'protein': meal['protein'],
#                 'carb': meal['carb'],
#                 'fat': meal['fat'],
#                 'notes': meal['notes']
#             }
#             simplified_day['meals'].append(simplified_meal)
#         simplified_plan.append(simplified_day)

#     return simplified_plan



"""
Install an additional SDK for JSON schema support Google AI Python SDK

$ pip install google.ai.generativelanguage
"""
def get_nutrition_plan(age, gender, height, weight, preference, allergy, activity_level, goal):
    import json
    import google.generativeai as genai
    from google.ai.generativelanguage_v1beta.types import content
    genai.configure(api_key="AIzaSyAZkHVWPbElqVdwXxbXtxN0q2rW8eqn_QI")
    prompt = f"أنشئ خطة غذائية باللغة العربية لمدة سبعة 7 أيام لشاب يبلغ من العمر {age} عاما، وزنه {weight} كغم وطوله {height} سم. هو {activity_level} ويريد {goal}. يفضل {preference} ولديه حساسية من {allergy}. يجب أن تحتوي كل وجبة على 400-500 سعرة حرارية ويجب أن تشمل البروتين العالي، الدهون المعتدلة، والكربوهيدرات المنخفضة. يجب تقسيم الوجبات إلى الإفطار والغداء والعشاء مع وجبتين خفيفتين يومياً. يرجى تقديم أحجام الوجبات لكل وجبة والتنوع في الوجبات. تأكد أن الخطة باللغة العربية ومؤلفة من سبعة 7 أيام."
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 40,
      "max_output_tokens": 2*8192,
      "response_schema": content.Schema(
        type = content.Type.OBJECT,
        description = "خطة غذائية باللغة العربية بسيطة ومتوازنة وصحية ومتنوعة لسبعة أيام تتلائم مع صفات المستخدم وتفضيلاته ومقسمة إلى وجبات إفطار وغداء وعشاء مع وجبتين خفيفتين يومياً مع تقديم أحجام الوجبات وقيمها الغذائية تأكد أن الخطة باللغة العربية وعدد الأيام سبعة.",
        enum = [],
        required = ["plan"],
        properties = {
          "plan": content.Schema(
            type = content.Type.ARRAY,
            items = content.Schema(
              type = content.Type.OBJECT,
              enum = [],
              required = ["day", "notes"],
              properties = {
                "day": content.Schema(
                  type = content.Type.ARRAY,
                  items = content.Schema(
                    type = content.Type.OBJECT,
                    enum = [],
                    required = ["day_num", "meal"],
                    properties = {
                      "day_num": content.Schema(
                        type = content.Type.INTEGER,
                      ),
                      "meal": content.Schema(
                        type = content.Type.ARRAY,
                        items = content.Schema(
                          type = content.Type.OBJECT,
                          enum = [],
                          required = ["name", "ingredients", "calorie", "protein", "carb", "fat", "notes"],
                          properties = {
                            "name": content.Schema(
                              type = content.Type.STRING,
                            ),
                            "ingredients": content.Schema(
                              type = content.Type.STRING,
                            ),
                            "calorie": content.Schema(
                              type = content.Type.INTEGER,
                            ),
                            "protein": content.Schema(
                              type = content.Type.INTEGER,
                            ),
                            "carb": content.Schema(
                              type = content.Type.INTEGER,
                            ),
                            "fat": content.Schema(
                              type = content.Type.INTEGER,
                            ),
                            "notes": content.Schema(
                              type = content.Type.STRING,
                            ),
                          },
                        ),
                      ),
                    },
                  ),
                ),
                "notes": content.Schema(
                  type = content.Type.STRING,
                ),
              },
            ),
          ),
        },
      ),
      "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
      model_name="gemini-2.0-flash",
      generation_config=generation_config,
    )

    chat_session = model.start_chat()

    response = chat_session.send_message(prompt)

    return json.loads(response.text)
'''
data = get_nutrition_plan(60, 1, 190, 33, "نباتي صرف'", "الغلوتين", 'نشيط جدًا (تمارس رياضة مكثفة يوميًا)', "بناء العضلات'")
plan = data["plan"]
for day_data in plan:
    # Each day has a 'day' (list of meals) and 'notes':
    meals = day_data["day"]
    day_notes = day_data["notes"]

    # 3. 'meals' is a list of day_num and meal:
    for meal_data in meals:
        day_num = meal_data["day_num"]
        meal_items = meal_data["meal"]  # List of meal items (breakfast, lunch, etc.)

        # 4. 'meal_items' contains the details of each meal:
        for meal_item in meal_items:
            name = meal_item["name"]
            ingredients = meal_item["ingredients"]
            calorie = meal_item["calorie"]
            protein = meal_item["protein"]
            carb = meal_item["carb"]
            fat = meal_item["fat"]
            notes = meal_item["notes"]

            # Now you have access to all the individual meal details
            print(f"Day: {day_num}, Meal: {name}")
            print(f"  Ingredients: {ingredients}")
            print(f"  Calories: {calorie}, Protein: {protein}, Carbs: {carb}, Fat: {fat}")
            print(f"  Notes: {notes}")
            print("-" * 20)

    print(f"Day Notes: {day_notes}")
    print("=" * 30)
'''