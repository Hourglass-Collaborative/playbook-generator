def format_html(user_name, organization_name, team_name, problem_statement, today):
    return """
        <!DOCTYPE html>
        <html lang="en" dir="ltr">
          <head>
            <meta charset="utf-8">
            <title>G.O.O.D. Innovation Playbook</title>
            <style>
              body {
                margin: 50px 50px 50px 50px;
                font-family: helvetica;
              }
              h1 {
                font-size: 20px;
              }
              h2 {
                font-size: 15px;
              }
              h3 {
                font-size: 12px;
              }
              h4 {
                font-size: 40px;
              }
              p {
                font-size: 12px;
              }
            </style>
          </head>"""+"""
          <body>
            <h2>{}, {}</h2>
            <h1>G.O.O.D. Innovation Playbook</h1>
            <p>Authored by: {} on {}</p>
            <hr></hr>
            <h3>Problem Definition</h3>
            <h4>{}</h4>
          </body>
        </html>
    """.format(organization_name, team_name, user_name, today, problem_statement)
