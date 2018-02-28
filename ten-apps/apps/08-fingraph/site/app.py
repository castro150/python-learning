# Boa prática no python: não usar o python local para rodar, porque tem dependências de outros
# projetos instaladas. Para isso, baixar a dependência virtualenv para virtualizar o python e
# usar no Heroku por exemplo, para isso é criada a pasta 'virtual' no projeto, com o comando
# 'virtualenv virtual', uma instalação isolada do python em 'virtual/bin/python'.
# IMPORTANTE: para instalar, usar o 'conda install venv'

# Para criar o requirements.txt: ../virtual/bin/pip freeze > requirements.txt
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/plot/')
def plot_endpoint():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    start = datetime.datetime(2016, 10, 1)
    end = datetime.datetime(2017, 3, 10)

    # name é o stock symbol da empresa (pesquisar no Google)
    df = data.DataReader(name="GOOG", data_source="quandl", start=start, end=end)

    p = figure(x_axis_type="datetime", width=1000, height=300, responsive=True)
    p.title.text = "Candlestick chart"
    p.grid.grid_line_alpha = 0

    hours_12 = 12 * 60 * 60 * 1000

    def inc_dec(c, o):
        if c > o:
            return "Increase"
        elif c < o:
            return "Decrease"
        return "Equal"

    df["Status"] = [inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"] = (df.Open + df.Close) / 2
    df["Height"] = abs(df.Open - df.Close)

    p.segment(df.index, df.High, df.index, df.Low, color="black")

    p.rect(df.index[df.Status == "Increase"], df.Middle[df.Status == "Increase"],
           hours_12, df.Height[df.Status == "Increase"], fill_color="#CCFFFF", line_color="black")

    p.rect(df.index[df.Status == "Decrease"], df.Middle[df.Status == "Decrease"],
           hours_12, df.Height[df.Status == "Decrease"], fill_color="#FF3333", line_color="black")

    script1, div1 = components(p)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files[0]
    return render_template("plot.html", script1=script1, div1=div1, cdn_js=cdn_js, cdn_css=cdn_css)

@app.route('/')
def home_endpoint():
    return render_template('home.html')


@app.route('/about')
def about_endpoint():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
