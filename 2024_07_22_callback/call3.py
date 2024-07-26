from dash import Dash,dcc,html,Input,Output,callback


external_stylesheets=''

app =Dash(__name__,external_stylesheets=external_stylesheets)

all_options={
    'A':{'NYC','SF','C'},
    'C':{'M','T','O'}
}

app.layout=html.Div([
    dcc.RadioItems(
        list(all_options.keys()),
        'A',
        id='country-radio'
    ),
    html.Hr(),
    dcc.RadioItems(id='city-radio'),
    html.Div(id='display-selected-values')
])
@callback(
    Output('city-radio','options'),
    Input('country-radio','value')
)
def set_city_options(selected_country:str):
    return [{'label':i,'value':i}for i in all_options[selected_country]]

@callback(
    Output('city-radio','value'),
    Input('city-radio','options') 
)
def set_city_value(available_options):
    return available_options[0]['value']

@callback(
    Output('display-selected-values','children'),
    Input('country-radio','value'),
    Input('city-radio','value')
)
def set_display_children(selected_country,selected_city):
    return f'{selected_city}位於{selected_country}'

if __name__ == "__main__":
    app.run(debug=True)