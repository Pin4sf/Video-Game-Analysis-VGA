import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import libraries.preprocessor as pp
import libraries.helper as hp

df = pp.preprocess(pd.read_csv('metacritic_2021.csv'))
dfp = pp.get_platforms(df)
tg = pp.top_games_meta(df)
tgu = pp.top_games_user(df)
gm = pp.grouped_critic(df)
um = pp.grouped_user(df)
gyc = pp.grouped_year_critic(df)
gyu = pp.grouped_year_user(df)
dfs = pd.read_csv('metacritic_2021.csv')

pc = hp.get_PC(df)
pc_summary = hp.get_PC_summary(pc)
pc_meta = hp.PC_meta_score(pc)
pc_user = hp.PC_user_review(pc)
c = hp.count(df)

psvxb = hp.get_PSvXB(df)
psvxb_count = hp.PSvXB_count(df)
psvxb_meta = hp.PSvXB_meta(psvxb)
psvxb_user = hp.PSvXB_user(psvxb)

xb = hp.get_XB(df)
xb_summary = hp.XB_summary(xb)
xb_by_year = hp.XB_by_year(xb)
xb_by_gen = hp.XB_by_gen(xb)
xb_top_meta = hp.XB_top_meta(xb)
xb_top_user = hp.XB_top_user(xb)

ps = hp.get_ps(df)
ps_summary = hp.PS_summary(ps)
ps_by_year = hp.PS_by_year(ps)
ps_by_gen = hp.PS_by_gen(ps)
ps_top_meta = hp.PS_top_meta(ps)
ps_top_user = hp.PS_top_user(ps)

st.set_page_config(
    page_title="VGA",
    page_icon="🎮",
)


st.sidebar.title('Video Game Analysis')
user_menu = st.sidebar.radio('Select', ("Data Cards📊", "Games Data Visualisation🀄", "Critics🧐 V/S Users😌","Xbox V/S PlayStation🎮"))

st.sidebar.success("Select to Explore from above ☝🏽.")

Year = st.sidebar.selectbox("Select year to get Game Of the year" , hp.year_of_GOTY(df))
year_input = Year
st.sidebar.write(hp.get_game_name_by_year(year_input, hp.game_of_the_year(df)))

if user_menu == "Data Cards📊":
    st.sidebar.subheader('Data Cards')
    st.title('Data 📊')
    st.write('##### In this page we are going to explore the metacritic data :sunglasses: ')
    st.markdown(''' 
                > This data contains the top games library of metacritic.
                >
                - We will compare the **critics and users score** of the games.
                - We will also compare the platforms and their games.
                >
                ''')
    st.markdown('<h2> Orignal Data </h2>', unsafe_allow_html=True)
    st.dataframe(df)
    st.write('Shape of the data is : ', df.shape)
    st.warning('You can get the summary of top games of entire data from the selectbox.')
    st.subheader('Top Games Summary')
    select_game = st.selectbox("Top Game Summary", pp.GName(df))
    st.text("Select a Game from above ☝🏽.")
    game_name = select_game
    game_summary = pp.get_game_summary(game_name, dfs)
    st.markdown('### **Game Summary**')
    st.write(game_summary)

    st.markdown('### **Unique Platforms**')
    st.markdown('Data contains following ***unique gaming platforms***')
    col1, col2, col3, col4, = st.columns(4) 
    col1.metric(label="PC", value="4,864", delta="1" )
    col2.metric(label="PlayStation 4", value="2,056", delta="2" , delta_color="inverse" )
    col3.metric(label="Xbox 360", value="1,644", delta="3", delta_color="inverse" )
    col4.metric(label="PlayStation 2", value="1,414", delta="4" , delta_color="inverse" )
    col5, col6, col7, col8, = st.columns(4)
    col5.metric(label="Switch", value="1,399", delta="5" )
    col6.metric(label="PlayStation 3", value="1,256", delta="6" , delta_color="inverse" )
    col7.metric(label="Xbox One", value="1,179", delta="7" , delta_color="inverse" )
    col8.metric(label="Xbox", value="789", delta="8" , delta_color="inverse" )
    col9, col10, col11, col12, = st.columns(4)
    col9.metric(label="DS", value="720", delta="9" , delta_color="inverse" )
    col10.metric(label="Wii", value="655", delta="10" , delta_color="inverse" )
    col11.metric(label="PSP", value="512", delta="11" , delta_color="inverse" )
    col12.metric(label="GameCube", value="448", delta="12" , delta_color="inverse" )
    col13, col14, col15, col16, = st.columns(4)
    col13.metric(label="GBA", value="438", delta="13" , delta_color="inverse" )
    col14.metric(label="3DS", value="396", delta="14" , delta_color="inverse" )
    col15.metric(label="PlayStation Vita", value="257", delta="15" , delta_color="inverse" )
    col16.metric(label="Playstation", value="187", delta="16" , delta_color="inverse")
    col17, col18, col19, col20, = st.columns(4)
    col17.metric(label="Wii U", value="184", delta="17" , delta_color="inverse")
    col18.metric(label="Dreamcast", value="125", delta="18" , delta_color="inverse")
    col19.metric(label="PlayStation 5", value="124", delta="19" )
    col20.metric(label="Xbox Serirs X", value="77", delta="20" )
    st.write(' >The consoles and devices marked in red are outdated and are not in production anymore.')
    st.markdown('### **Top 25 Games by Meta Score**')
    st.dataframe(tg)
    st.markdown('### **Top 25 Games by User Score**')
    st.dataframe(tgu)
    st.caption('This is just a preview of the data we are going to get a better analysis in the next pages.')
    code= ''' For 'data visualisation' go to next page from sidebar 👈🏽 '''
    st.code(code, language='python')

elif user_menu == "Games Data Visualisation🀄":
    st.title('Data Visualisation 🀄')
    st.sidebar.subheader('Data Visualisation')
    st.caption('Some Total Stats of the data 📄')
    col1, col2 , col3= st.columns(3)
    with col1:
        st.subheader('Total Games')
        st.title('12,254')
    with col2:
        st.subheader('Total Platforms')
        st.title('22')
    with col3:
        st.subheader('Total Years')
        st.title('23')
    fig = px.bar(dfp, x="Count", y="Platform", orientation="h", color="Platform")
    fig.update_layout(
    title="Platform Count",
    title_font=dict(size=16, color="purple"),
    yaxis=dict(title="Platform"),
    xaxis=dict(title="Count"),
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig)
    st.markdown("As you can see we have a lot of different types of gaming platforms throughout the years of progression but we will focus on some of the most prominent platforms which aren't handheld.")
    st.markdown("""
> ##### These are the platforms we are going to focus on:
>
>- **PC**
>- **PlayStation**
>- **Xbox**
""")

    st.write(" ##### We will compare the games counts of these platforms.")
    platforms = ['PC', 'PlayStation', 'Xbox']
    counts = [4612, 4547, 3249]
    colors = ['maroon', 'teal', 'green']
    
    fig1= go.Figure(data=[go.Bar(x=platforms, y=counts, marker=dict(color=colors))])
    
    fig1.update_layout(
        title='Number of Games by Platform',
        title_font=dict(size=16, color='purple'),
        yaxis=dict(title='Count'),
        xaxis=dict(title='Platform'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig1)
    vxb1 = go.Figure(data=go.Pie(
    labels=c.index,
    values=c.Count,
    textinfo='percent',
    hoverinfo='label+percent',
    textfont=dict(size=14),
    marker=dict(line=dict(color='white', width=1)),
    ))
    st.write(" As we can observe that PC and PlayStation have the most number of games compared to XBOX reason is that these are the platforms which are bexisting from 90's and XBOX made its debute in the market around 2000 this explains the smaller library but in recent year all the major games seems to be launching on all these platforms.")

    vxb1.update_layout(
        title='Percentage of Games by Platform',
        title_font=dict(size=16, color='purple'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(vxb1)
    st.write(" We observe that PC have the highest percentage of games so let's dive deeper into the PC games.")
    st.subheader('Analysing PC games data')
    st.caption('PC games data')
    st.dataframe(pc)
    st.markdown('##### *Getting Summary From data using Numpy*')
    st.write(pc_summary)
    pc1 = go.Figure()
    
    pc1.add_trace(go.Box(
        y=pc['meta_score'],
        name='Metascore',
        marker=dict(color='teal'),
        boxmean=True,
    ))
    
    pc1.add_trace(go.Box(
        y=pc['user_review'],
        name='User Review',
        marker=dict(color='crimson'),
        boxmean=True,
    ))
    
    pc1.update_layout(
        title='PC Game Scores',
        title_font=dict(size=16, color='purple'),
        yaxis=dict(title='Score'),
        xaxis=dict(title='Score Type'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    st.plotly_chart(pc1)
    st.caption('We can see that the average score of the games is for Critics and User is same around 7.0 but user data seems to have much more outliers.')
    st.text('I have segerated the required data from the main datain the helper.py file.')
    st.markdown('The data jupyter notebook can be accessed via [Github](https://github.com/Pin4sf/Video-Game-Analysis-VGA) .')
    pc2 = go.Figure()
    
    pc2.add_trace(go.Scatter(
        x=pc_meta.index,
        y=pc_meta,
        mode='lines',
        line=dict(color='teal'),
        name='Metascore'
    ))
    
    pc2.add_trace(go.Scatter(
        x=pc_user.index,
        y=pc_user,
        mode='lines',
        line=dict(color='crimson'),
        name='User Score'
    ))
    
    pc2.update_layout(
        title='Average Critic and User Scores by Year for PC Games',
        title_font=dict(size=16, color='purple'),
        xaxis=dict(title='Year'),
        yaxis=dict(title='Average Score'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=True
    )
    st.plotly_chart(pc2)
    st.markdown(""" 
Earier Critics and Users were havinh similar opinion and ratings regarding games but recent decade we can obsereve that the critics and users have different opinions and ratings regarding games.

***Critics*** are more focused on the ***technical aspects*** of the game and the ***users*** are more focused on the gameplay and the ***overall experience*** of the game. This explains why Users in recent years are having much more lower ratings than Critics.

> This is some intresting trend between critics and user.

""")
    code= ''' Let's Deep dive into "Critics v/s User" go to next section from sidebar 👈🏽 '''
    st.code(code, language='python')

elif user_menu == "Critics🧐 V/S Users😌":
    st.title('Critics🧐 V/S Users😌')
    st.sidebar.subheader('Critics V/S Users')
    st.write('#### In this page we are going to compare the critics and users score of the games :sunglasses: ')
    st.markdown(' > First we need to get the data of Critics and Users from the main data.')

    st.markdown('#### **Analysing Critics and Users Data**')

    fig2 = go.Figure()
    
    fig2.add_trace(go.Histogram(x=df['meta_score'], nbinsx=100, marker=dict(color='teal'), 
                                opacity=0.75, name='Metascore'))
    
    fig2.add_trace(go.Histogram(x=df['user_review'], nbinsx=100, marker=dict(color='crimson'), 
                                opacity=0.75, name='User Score'))
    
    fig2.update_layout(
        title='Distribution of Critic and User Scores by count',
        title_font=dict(size=16 , color='purple'),
        xaxis=dict(title='Score'),
        yaxis=dict(title='Count'),
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(fig2)
    st.markdown('We can observe that the distribution of the scores is similar for both the critics and users with respect to count.')
    st.write(' Ploting the Joint Distribution of the scores. (Because it is cool & easier to understand) :fire: ')
    fig3 = go.Figure(data=go.Histogram2dContour(
    x=df['meta_score'],
    y=df['user_review'],
    colorscale='Viridis',
    contours=dict(coloring='heatmap'),
    hovertemplate='Meta Score: %{x}<br>User Review: %{y}<br>Count: %{z}<extra></extra>'
    ))

    fig3.update_layout(
        title='Joint Distribution of Critic and User Scores',
        title_font=dict(size=16, color='purple'),
        xaxis=dict(title='Meta Score'),
        yaxis=dict(title='User Review'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        coloraxis_colorbar=dict(title='Count'),
    )
    st.plotly_chart(fig3)

    st.markdown('Moving forward lets compare the average scores of the games by critics and users accross different consoles .')
    
    fig4 = go.Figure()
    
    fig4.add_trace(go.Bar(
        x=gm.index,
        y=gm,
        marker=dict(color='teal'),
        opacity=0.75,
        name='Metascore'
    ))
    
    fig4.add_trace(go.Bar(
        x=um.index,
        y=um,
        marker=dict(color='crimson'),
        opacity=0.75,
        name='User Score'
    ))
    
    fig4.update_layout(
        title='Average Critic and User Scores by Platform',
        title_font=dict(size=16, color='purple'),
        xaxis=dict(title='Platform'),
        yaxis=dict(title='Average Score'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        barmode='group'
    )
    st.plotly_chart(fig4)
    st.write(" Well the ratings are pritty much consistent across different platforms between users and critics but we can observe that ***Nintendo 64 🕹️*** have the highest average score for both the critics and users. This might be because it's one of the *earliest consoles* and defined gaming industry they have some of the old and gold standard titles like **Mario** , **Donkey Kong** and many others")

    st.markdown('> **Analysing Critics and Users Data by Year**')
    fig5 = go.Figure()
    
    fig5.add_trace(go.Scatter(
        x=gyc.index,
        y=gyc,
        mode='lines',
        line=dict(color='teal'),
        name='Metascore'
    ))
    
    fig5.add_trace(go.Scatter(
        x=gyu.index,
        y=gyu,
        mode='lines',
        line=dict(color='crimson'),
        name='User Score'
    ))
    
    fig5.update_layout(
        title='Average Critic and User Scores by Year',
        title_font=dict(size=16, color='purple'),
        xaxis=dict(title='Year'),
        yaxis=dict(title='Average Score'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=True
    )
    
    st.plotly_chart(fig5)
    st.markdown(""" 
> This is similar trend as we have observed in the PC games data.

Earier Critics and Users were havinh similar opinion and ratings regarding games but recent decade we can obsereve that the critics are having much more higher scores and users are not much satisfied as we see a consistent fall in ratings.

""")
    
    st.markdown('#### Analysing the **Top Games** by Critic and User Reviews')
    figa = go.Figure()
    
    figa.add_trace(go.Scatter(
        x=tg['meta_score'],
        y=tg['name'],
        mode='markers',
        marker=dict(color='teal', size=12),
        name='Metascore'
    ))
    
    figa.add_trace(go.Scatter(
        x=tgu['user_review'],
        y=tgu['name'],
        mode='markers',
        marker=dict(color='crimson', size=12),
        name='User Score'
    ))
    
    figa.update_layout(
        title='Top Games by Critic and User Reviews',
        title_font=dict(size=16, color='purple'),
        xaxis=dict(title='Score'),
        yaxis=dict(title='Name'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(figa)
    st.success('To get better view of top games of individual group toggle the legend in above graph.')

elif user_menu == "Xbox V/S PlayStation🎮":
    st.title('Xbox V/S PlayStation🎮')
    st.sidebar.subheader('Xbox V/S PlayStation')
    st.write('##### In this page we are going to compare the Xbox and PlayStation games :sunglasses: ')
    st.markdown(' > First we need to get the data of Xbox and PlayStation games from the main data.')
    st.text('Then we will compare the data of both the platforms.')
    st.write('##### Getting the data of Xbox and PlayStation games.')
    st.info('Toggle the tabs to get the data of Xbox and PlayStation games.')
    tab1 , tab2 = st.tabs(['PlayStation', 'Xbox'])
    with tab1 :
        st.title('PlayStation Games')
        st.dataframe(ps)
    with tab2 :
        st.title('Xbox Games')
        st.dataframe(xb)
    
    platforms = [ 'PlayStation', 'Xbox']
    counts = [ 4547, 3249]
    colors = ['teal', 'green']
    figpx= go.Figure(data=[go.Bar(x=platforms, y=counts, marker=dict(color=colors))])
    
    figpx.update_layout(
        title='Number of Games by Platform',
        title_font=dict(size=16, color='purple'),
        yaxis=dict(title='Count'),
        xaxis=dict(title='Platform'),
        height=500,
        width=650,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(figpx)
    st.warning('We have dropped the PlayStation Vita and PSP as they are handheld consoles and was not required for comparasion.')
    st.markdown('We observe that the number of PlayStation games are more than Xbox games. That means Playstation have current lead in games library but recently Xbox has launched its new console Xbox Series X and Xbox Series S giving Playstation 5 tough competetion in games exclusivity.')
    st.markdown('## **Analysing PlayStation Games and Xbox Games**')
    colp ,colx = st.columns(2)
    with colp :
        st.subheader('PlayStation Games')
        st.write(ps_summary)
    with colx :
        st.subheader('Xbox Games')
        st.write(xb_summary)
    st.header('Analysis Tabs')
    tabp , tabx = st.tabs(['PlayStation', 'Xbox'])
    with tabp :
        st.caption('PlayStation games data')
        col1a , col2a = st.columns(2)
        with col1a :
            st.markdown('##### **PlayStation Games by Year**')
            st.dataframe(ps_by_year)
        with col2a :
            st.markdown('##### **PlayStation Games by *Gen***')
            st.dataframe(ps_by_gen)
        st.markdown('### **PlayStation Games by Meta Score v/s User Score**')
        figps1 = go.Figure()
        figps1.add_trace(go.Box(
            y=ps['meta_score'],
            name='Metascore',
            marker=dict(color='purple'),
            boxmean=True,
            boxpoints='outliers',
            jitter=0.3,
            pointpos=-1.8,
        ))
        
        figps1.add_trace(go.Box(
            y=ps['user_review'],
            name='User Review',
            marker=dict(color='pink'),
            boxmean=True,
            boxpoints='outliers',
            jitter=0.3,
            pointpos=-1.8,
        ))
        
        figps1.update_layout(
            title='PlayStation PlotBox',
            title_font=dict(size=16, color='purple'),
            yaxis=dict(title='Score'),
            xaxis=dict(title='PlayStation'),
            height=500,
            width=700,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(figps1)
        st.write('The distribution of ratings is kinda similar but we can observe that the user scores are much more varying and all over the place thus more outliers.')
        st.markdown('### **PlayStation User and Critics by Year**')
        figps2 = go.Figure()
        figps2.add_trace(go.Bar(
            x=ps_by_year['year'],
            y=ps_by_year['meta_score'],
            name='Metascore',
            marker=dict(color='teal')
        ))
        
        figps2.add_trace(go.Bar(
            x=ps_by_year['year'],
            y=ps_by_year['user_review'],
            name='User Review',
            marker=dict(color='crimson')
        ))
        
        figps2.update_layout(
            title="PlayStation's Scores by Year",
            title_font=dict(size=16, color='purple'),
            xaxis=dict(title='Year'),
            yaxis=dict(title='Score'),
            height=500,
            width=650,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            barmode='group'
        )
        st.plotly_chart(figps2)
        st.markdown('### **PlayStation User and Critics by Gen**')
        figps3 = go.Figure()
        figps3.add_trace(go.Bar(
            x=ps_by_gen['platform'],
            y=ps_by_gen['meta_score'],
            name='Metascore',
            marker=dict(color='teal')
        ))
        
        figps3.add_trace(go.Bar(
            x=ps_by_gen['platform'],
            y=ps_by_gen['user_review'],
            name='User Review',
            marker=dict(color='crimson')
        ))
        
        figps3.update_layout(
            title="PlayStation's Scores by Gen",
            title_font=dict(size=16, color='purple'),
            xaxis=dict(title='Platform'),
            yaxis=dict(title='Score'),
            height=500,
            width=650,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            barmode='group'
        )
        st.plotly_chart(figps3)
        st.markdown("""
During initial years of Playstation Users seem to have much more average score than critics and around Playstation 2 users seem to enjoy the games more than critics but in last two generations of Playstation critics are having much more higher average score than users.

Regardless the ratings of games it is clear that Playstation is the most popular gaming console in the world and have the most number of games library, recent consoles are much more advanced and have more complex games.
""")
        st.subheader('Top PS games by User and Critics')
        col1b , col2b = st.columns(2)
        with col1b :
            st.markdown('##### **PlayStation Games by Meta Score**')
            st.dataframe(ps_top_meta)
        with col2b :
            st.markdown('##### **PlayStation Games by User Score**')
            st.dataframe(ps_top_user)
            
        figps4 = go.Figure()
        figps4.add_trace(go.Scatter(
            x=ps_top_meta['meta_score'],
            y=ps_top_meta['name'],
            mode='markers',
            marker=dict(color='teal', size=12),
            name='Metascore'
        ))
        
        figps4.add_trace(go.Scatter(
            x=ps_top_user['user_review'],
            y=ps_top_user['name'],
            mode='markers',
            marker=dict(color='crimson', size=12),
            name='User Score'
        ))
        
        figps4.update_layout(
            title='Top Games by Critic and User Reviews',
            title_font=dict(size=16, color='purple'),
            xaxis=dict(title='Score'),
            yaxis=dict(title='Name'),
            height=500,
            width=700,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(figps4)

    with tabx:
        st.caption('Xbox games data')
        col1c , col2c = st.columns(2)
        with col1c :
            st.markdown('##### **Xbox Games by Year**')
            st.dataframe(xb_by_year)
        with col2c :
            st.markdown('##### **Xbox Games by *Gen***')
            st.dataframe(xb_by_gen)
        st.markdown('### **Xbox Games by Meta Score v/s User Score**')
        figxb1 = go.Figure()
        figxb1.add_trace(go.Box(
            y=xb['meta_score'],
            name='Metascore',
            marker=dict(color='purple'),
            boxmean=True,
            boxpoints='outliers',
            jitter=0.3,
            pointpos=-1.8,
        ))
        
        figxb1.add_trace(go.Box(
            y=xb['user_review'],
            name='User Review',
            marker=dict(color='pink'),
            boxmean=True,
            boxpoints='outliers',
            jitter=0.3,
            pointpos=-1.8,
        ))
        
        figxb1.update_layout(
            title='Xbox PlotBox',
            title_font=dict(size=16, color='purple'),
            yaxis=dict(title='Score'),
            xaxis=dict(title='Xbox'),
            height=500,
            width=700,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(figxb1)
        st.write('The distribution of ratings is kinda ***similar*** to that of **PC** and **PlayStation** but we can observe that the user scores are much more varying and all over the place thus more outliers.')
        st.markdown('### **Xbox User and Critics by Year**')
        figxb2 = go.Figure()
        figxb2.add_trace(go.Bar(
            x=xb_by_year['year'],
            y=xb_by_year['meta_score'],
            name='Metascore',
            marker=dict(color='teal')
        ))
        
        figxb2.add_trace(go.Bar(
            x=xb_by_year['year'],
            y=xb_by_year['user_review'],
            name='User Review',
            marker=dict(color='crimson')
        ))
        
        figxb2.update_layout(
            title="Xbox's Scores by Year",
            title_font=dict(size=16, color='purple'),
            xaxis=dict(title='Year'),
            yaxis=dict(title='Score'),
            height=500,
            width=650,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            barmode='group'
        )
        st.plotly_chart(figxb2)
        st.markdown('### **Xbox User and Critics by Gen**')
        figxb3 = go.Figure()
        figxb3.add_trace(go.Bar(
            x=xb_by_gen['platform'],
            y=xb_by_gen['meta_score'],
            name='Metascore',
            marker=dict(color='teal')
        ))
        figxb3.add_trace(go.Bar(
            x=xb_by_gen['platform'],
            y=xb_by_gen['user_review'],
            name='User Review',
            marker=dict(color='crimson')
        ))
        figxb3.update_layout(
            title="Xbox's Scores by Gen",
            title_font=dict(size=16, color='purple'),
            xaxis=dict(title='Platform'),
            yaxis=dict(title='Score'),
            height=500,
            width=650,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            barmode='group'
        )
        st.plotly_chart(figxb3)
        st.markdown("""
The trend of Xbox is been consistent throughout the years with a constant growth rate with each new generation and in recent years they have really amped up the gaming industry space with good games and powerful consoles.
                    
It can be seen that critics are liking Xbox games much more in latest generation Xbox Series X and S consoles.
> Xbox is the only console which is giving Playstation a tough competetion in the gaming industry.
""")
        st.subheader('Top Xbox games by User and Critics')
        col1d , col2d = st.columns(2)
        with col1d :
            st.markdown('##### **Xbox Games by Meta Score**')
            st.dataframe(xb_top_meta)
        with col2d :
            st.markdown('##### **Xbox Games by User Score**')
            st.dataframe(xb_top_user)
        
        figxb4 = go.Figure()
        figxb4.add_trace(go.Scatter(
            x=xb_top_meta['meta_score'],
            y=xb_top_meta['name'],
            mode='markers',
            marker=dict(color='teal', size=12),
            name='Metascore'
        ))

        figxb4.add_trace(go.Scatter(
            x=xb_top_user['user_review'],
            y=xb_top_user['name'],
            mode='markers',
            marker=dict(color='crimson', size=12),
            name='User Score'
        ))

        figxb4.update_layout(
            title='Top Games by Critic and User Reviews',
            title_font=dict(size=16, color='purple'),
            xaxis=dict(title='Score'),
            yaxis=dict(title='Name'),
            height=500,
            width=700,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(figxb4)

    st.markdown('# **Comparing Recent 2 generation of PlayStation and Xbox**')
    st.text('loading the data of PlayStation 4 & PlayStation 5 and Xbox One & Xbox Series X')
    st.dataframe(psvxb)
    st.markdown('### ***Getting Count of these Consoles from data***')
    colps4, colps5, colxbo, colxbx, = st.columns(4) 
    colps4.metric(label="Playstation 4", value="2,056", delta="1" )
    colps5.metric(label="PlayStation 5", value="124", delta="2"  )
    colxbo.metric(label="Xbox One", value="1,179", delta="3" )
    colxbx.metric(label="Xbox Series X", value="77", delta="4"  )
    figpsvxb1 = go.Figure(data=go.Pie(
    labels=psvxb_count.index,
    values=psvxb_count.Count,
    textinfo='percent',
    hoverinfo='label+percent',
    textfont=dict(size=14),
    marker=dict(line=dict(color='white', width=1)),
    ))

    figpsvxb1.update_layout(
        title='Percentage of Games by Platform',
        title_font=dict(size=16, color='purple'),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    st.plotly_chart(figpsvxb1)
    st.markdown('The current dominance of PlayStation is clearly visible in the data as it has more than 80% of the games in the consoles. But recent Xbox generation is really giving Playstation a tough competetion.')
    st.markdown('#### **Getting Top Meta Score and User voted Games of Both Platforms**')
    metatab , usertab = st.tabs(['Meta Score', 'User Score'])
    with metatab :
        st.markdown('##### **Top Meta Score Games**')
        st.table(psvxb_meta)
    with usertab :
        st.markdown('##### **Top User Score Games**')
        st.table(psvxb_user)
    code= ''' Lets see what happen next in "gaming industry it is one of the most fascinating 
    and fastest growing industry" in the world. It will be intresting to see 
    what new consoles and games we will get in future. '''
    st.code(code, language='python')

    st.markdown('## Thats all for now. Thank you for reading. :smile:')
    st.markdown(
    """
    <div align="center">
    <h4>Made with ❤️ by Pin4sf<h4>
    </div>
    """, unsafe_allow_html=True,)



