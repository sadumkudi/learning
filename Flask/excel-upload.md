modules installed:
  1. flask
  2. pandas
        data = pd.read_excel(file)
        return render_template('data.html', data=data.to_html())

  3. xlrd - for Excel support
