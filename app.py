from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
import folium
from bs4 import BeautifulSoup
import re
import pandas as pd

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    text = request.form['text']

    url = "https://www.emploitic.com/offres-d-emploi?q="
    url = url + text
    doc = BeautifulSoup(url, "lxml")

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.0 Safari/537.36'}
    response = requests.get(url, headers=headers)
    result = BeautifulSoup(response.content, "lxml")
    cont = result.find_all('script')
    varr = str(cont[19])
    urls = re.findall('(?P<url>https://www.emploitic.com/offres-d-emploi/offre-d-emploi/algerie/[0-9a-z/-]+)', varr)#[a-zA-Z0-9-]

    location_job_list = []
    for i in urls:
        remover= i[65:]
        location_job_list.append(remover)
    job_title = []
    cleaned_list = [i.split('/') for i in location_job_list]
    for i in cleaned_list:
        if len(i)==3:
            del i[1]
        if len(i)==1:
            del i
    df = pd.DataFrame(cleaned_list)
    df[1] = df[1].str.replace(r'[\d+-]', ' ')
    df['Address'] = urls
    df.columns = ['location', 'job_title', "adress"]
    df.dropna(inplace=True)


    wilaya = [
    {"id":"1","code":"1","name":"Adrar", "ar_name":"أدرار", "latitude":"27.9766155", "longitude":"-0.20396"},
    {"id":"2","code":"2","name":"Chlef", "ar_name":"الشلف", "latitude":"36.1691245", "longitude":"1.3539002"},
    {"id":"3","code":"3","name":"Laghouat", "ar_name":"الأغواط", "latitude":"33.7873735", "longitude":"2.8829115"},
    {"id":"4","code":"4","name":"Oum El Bouaghi", "ar_name":"أم البواقي", "latitude":"35.8726014", "longitude":"7.1180248"},
    {"id":"5","code":"5","name":"Batna", "ar_name":"باتنة", "latitude":"35.32147", "longitude":"3.1066502"},
    {"id":"6","code":"6","name":"Bejaia", "ar_name":"بجاية", "latitude":"36.7695969", "longitude":"5.0085855"},
    {"id":"7","code":"7","name":"Biskra", "ar_name":"بسكرة", "latitude":"34.8515041", "longitude":"5.7246709"},
    {"id":"8","code":"8","name":"Bechar", "ar_name":"بشار", "latitude":"31.5977602", "longitude":"-1.8540446"},
    {"id":"9","code":"9","name":"Blida", "ar_name":"البليدة", "latitude":"36.4803023", "longitude":"2.8009379"},
    {"id":"10","code":"10","name":"bouira", "ar_name":"البويرة", "latitude":"36.2084234", "longitude":"3.925049"},
    {"id":"11","code":"11","name":"Tamanrasset", "ar_name":"تمنراست", "latitude":"22.2746227", "longitude":"5.6754684"},
    {"id":"12","code":"12","name":"Tbessa", "ar_name":"تبسة", "latitude":"35.4117259", "longitude":"8.110545"},
    {"id":"13","code":"13","name":"Tlemcen", "ar_name":"تلمسان", "latitude":"34.8959541", "longitude":"-1.3150979"},
    {"id":"14","code":"14","name":"Tiaret", "ar_name":"تيارت", "latitude":"35.3599899", "longitude":"1.3916159"},
    {"id":"15","code":"15","name":"Tizi Ouzou", "ar_name":"تيزي وزو", "latitude":"36.7002068", "longitude":"4.075957"},
    {"id":"16","code":"16","name":"alger", "ar_name":"الجزائر", "latitude":"36.7538259", "longitude":"3.057841"},
    {"id":"17","code":"17","name":"Djelfa", "ar_name":"الجلفة", "latitude":"34.6672467", "longitude":"3.2993118"},
    {"id":"18","code":"18","name":"Jijel", "ar_name":"جيجل", "latitude":"36.7962714", "longitude":"5.7504845"},
    {"id":"19","code":"19","name":"Se9tif", "ar_name":"سطيف", "latitude":"36.1905173", "longitude":"5.4202134"},
    {"id":"20","code":"20","name":"Saida", "ar_name":"سعيدة", "latitude":"34.841945", "longitude":"0.1483583"},
    {"id":"21","code":"21","name":"Skikda", "ar_name":"سكيكدة", "latitude":"36.8777912", "longitude":"6.9357204"},
    {"id":"22","code":"22","name":"Sidi Bel Abbes", "ar_name":"سيدي بلعباس", "latitude":"35.206334", "longitude":"-0.6301368"},
    {"id":"23","code":"23","name":"Annaba", "ar_name":"عنابة", "latitude":"36.9184345", "longitude":"7.7452755"},
    {"id":"24","code":"24","name":"Guelma", "ar_name":"قالمة", "latitude":"36.4569088", "longitude":"7.4334312"},
    {"id":"25","code":"25","name":"Constantine", "ar_name":"قسنطينة", "latitude":"36.319475", "longitude":"6.7370571"},
    {"id":"26","code":"26","name":"Medea", "ar_name":"المدية", "latitude":"36.2838408", "longitude":"2.7728462"},
    {"id":"27","code":"27","name":"Mostaganem", "ar_name":"مستغانم", "latitude":"35.9751841", "longitude":"0.1149273"},
    {"id":"28","code":"28","name":"MSila", "ar_name":"المسيلة", "latitude":"35.7211476", "longitude":"4.5187283"},
    {"id":"29","code":"29","name":"Mascara", "ar_name":"معسكر", "latitude":"35.382998", "longitude":"0.1542592"},
    {"id":"30","code":"30","name":"Ouargla", "ar_name":"ورقلة", "latitude":"32.1961967", "longitude":"4.9634113"},
    {"id":"31","code":"31","name":"Oran", "ar_name":"وهران", "latitude":"35.7066928", "longitude":"-0.6405861"},
    {"id":"32","code":"32","name":"El Bayadh", "ar_name":"البيض", "latitude":"32.5722756", "longitude":"0.950011"},
    {"id":"33","code":"33","name":"Illizi", "ar_name":"إليزي", "latitude":"26.5065999", "longitude":"8.480587"},
    {"id":"34","code":"34","name":"Bordj Bou Arreridj", "ar_name":"برج بوعريريج", "latitude":"36.0686488", "longitude":"4.7691823"},
    {"id":"35","code":"35","name":"Boumerdes", "ar_name":"بومرداس", "latitude":"36.7564181", "longitude":"3.4917212"},
    {"id":"36","code":"36","name":"El Tarf", "ar_name":"الطارف", "latitude":"36.7534258", "longitude":"8.2984543"},
    {"id":"37","code":"37","name":"Tindouf", "ar_name":"تندوف", "latitude":"27.2460501", "longitude":"-6.3252899"},
    {"id":"38","code":"38","name":"Tissemsilt", "ar_name":"تيسمسيلت", "latitude":"35.6021906", "longitude":"1.802187"},
    {"id":"39","code":"39","name":"El Oued", "ar_name":"الوادي", "latitude":"33.3714492", "longitude":"6.8573436"},
    {"id":"40","code":"40","name":"Khenchela", "ar_name":"خنشلة", "latitude":"35.4263293", "longitude":"7.1414137"},
    {"id":"41","code":"41","name":"Souk Ahras", "ar_name":"سوق أهراس", "latitude":"36.277849", "longitude":"7.9592299"},
    {"id":"42","code":"42","name":"Tipaza", "ar_name":"تيبازة", "latitude":"36.5980966", "longitude":"2.4085379"},
    {"id":"43","code":"43","name":"Mila", "ar_name":"ميلة", "latitude":"36.4514882", "longitude":"6.2487316"},
    {"id":"44","code":"44","name":"Ain Defla", "ar_name":"عين الدفلى", "latitude":"36.1283915", "longitude":"2.1772514"},
    {"id":"45","code":"45","name":"Naama", "ar_name":"النعامة", "latitude":"33.1995605", "longitude":"-0.8021968"},
    {"id":"46","code":"46","name":"Ain Temouchent", "ar_name":"عين تموشنت", "latitude":"35.404044", "longitude":"-1.0580975"},
    {"id":"47","code":"47","name":"Ghardaia", "ar_name":"غرداية", "latitude":"32.5891743", "longitude":"3.7455655"},
    {"id":"48","code":"48","name":"Relizane", "ar_name":"غليزان", "latitude":"35.8050195", "longitude":"0.867381"},
    {"id":"49","code":"49","name":"El M'ghair", "ar_name":"المغير", "latitude":"33.947222", "longitude":"5.922222"},
    {"id":"50","code":"50","name":"El Menia", "ar_name":"المنيعة", "latitude":"30.579167", "longitude":"2.879167"},
    {"id":"51","code":"51","name":"Ouled Djellal", "ar_name":"أولاد جلال", "latitude":"34.433333", "longitude":"5.066667"},
    {"id":"52","code":"52","name":"Bordj Baji Mokhtar", "ar_name":"برج باجي مختار", "latitude":"21.327778", "longitude":"0.955556"},
    {"id":"53","code":"53","name":"Beni Abbes", "ar_name":"بني عباس", "latitude":"30.133333", "longitude":"-2.166667"},
    {"id":"54","code":"54","name":"Timimoun", "ar_name":"تيميمون", "latitude":"29.258333", "longitude":"0.230556"},
    {"id":"55","code":"55","name":"Touggourt", "ar_name":"تقرت", "latitude":"33.108333", "longitude":"6.063889"},
    {"id":"56","code":"56","name":"Djanet", "ar_name":"جانت", "latitude":"24.554167", "longitude":"9.484722"},
    {"id":"57","code":"57","name":"In Salah", "ar_name":"عين صالح", "latitude":"27.197222", "longitude":"2.483333"},
    {"id":"58","code":"58","name":"In Guezzam", "ar_name":"عين قزام", "latitude":"19.572222", "longitude":"5.769444"}]


    wil = pd.DataFrame(wilaya)
    wil1 = wil[["name", "latitude", "longitude"]]
    wil1.columns = ["location", "latitude", "longitude"]
    wil1["location"] = wil1["location"].str.lower()
    merg = pd.merge(df, wil1)
    merg["link"]='<li><a href=' +merg["adress"]+ '>'+merg["job_title"]+'</a></li>'
    final_df = merg.groupby(["location", "latitude", "longitude"])['link'].apply(lambda x: ''.join(x.astype(str))).reset_index()

    m = folium.Map(location=[36.7538259,3.057841], tiles="Stamen Toner", zoom_start=7)
    final_df.apply(lambda row:folium.Marker(location=[row["latitude"], row["longitude"]],
                                              radius=10, tooltip = str(len(re.findall("<li>", row["link"])))+" offer(s)", popup="<b>"+row["location"]+":"+"<b/>"+row["link"], icon=folium.Icon(color='red', icon='fa-map-pin', prefix='fa'))
                                             .add_to(m), axis=1)
    search_box = '''
      <form method="POST">
        <input name="text">
        <input type="submit" value="Enter Job Title" />
      </form>
    '''
    return search_box + m._repr_html_()
if __name__ == "__main__":
            app.run(debug=True)
