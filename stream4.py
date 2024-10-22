import streamlit as st
import plotly.graph_objects as go

# Define the textile trade routes (updated with locations and interconnections)
textile_trade_routes = {
    "India to England": [(72.8777, 19.0760, "India (Gujarat)"), (-0.1276, 51.5074, "London")],
    "India to Africa": [(72.8777, 19.0760, "India (Gujarat)"), (-16.6169, 13.4432, "Gambia")],
    "West Africa to the Americas": [(-16.6169, 13.4432, "West Africa (Gambia)"), (-81.6556, 30.3322, "American South")],
    "United States to England": [(-81.6556, 30.3322, "American South"), (-2.2426, 53.4808, "Manchester")],
    "Mexico to Spain": [(96.7266, 17.0759, "Mexico (Oaxaca)"), (-5.9845, 37.3891, "Seville")],
    "Peru to Spain": [(-77.0428, -12.0464, "Peru"), (-5.9845, 37.3891, "Seville")],
    "England to Europe": [(-2.2426, 53.4808, "Manchester"), (2.3522, 48.8566, "Paris")],
    "France to West Africa": [(2.3522, 48.8566, "Paris"), (-16.6169, 13.4432, "West Africa (Gambia)")],
    "India to China": [(88.3639, 22.5726, "India (Bengal)"), (104.1954, 35.8617, "China (Shanghai)")],
    "China to Europe": [(104.1954, 35.8617, "China (Shanghai)"), (2.3522, 48.8566, "Paris")],
    "Caribbean to Spain": [(-61.0588, 13.9094, "Caribbean"), (-5.9845, 37.3891, "Seville")],
    "Brazil to Portugal": [(-38.5014, -12.9714, "Brazil"), (-9.1393, 38.7223, "Lisbon")],
    "England to India": [(-2.2426, 53.4808, "Manchester"), (88.3639, 22.5726, "India (Bengal)")],
    "Spain to the Netherlands": [(-5.9845, 37.3891, "Seville"), (4.9041, 52.3676, "Netherlands")]
}

dye_trade_routes = {
    "Indigo": [
        (78.9629, 20.5937, "India - Origin and Production"),  # Indigo originated and was produced in India
        (-9.1393, 38.7223, "Lisbon - Portuguese Trade Hub"),  # Lisbon was a key trade hub for Europe
        (4.4024, 51.2194, "Antwerp - European Distribution"),  # Antwerp served as a key distribution center
        (-0.1276, 51.5074, "London - British Textile Industry"),  # Reached London for use in textile production
        (2.3522, 48.8566, "France - French Textile Industry"),  # Used in France’s textile industry
        (12.4964, 41.9028, "Italy - Italian Textile Industry"),  # Reached Italy for further use
        (4.9041, 52.3676, "Netherlands - Dutch Textile Industry")  # Distributed in the Netherlands
    ],

    "Cochineal": [
        (-96.7266, 17.0759, "Oaxaca, Mexico - Origin and Production"),  # Cochineal was produced in Oaxaca, Mexico
        (-96.1429, 19.1738, "Veracruz - Export Hub"),  # Exported from Veracruz
        (-5.9845, 37.3891, "Seville - Spanish Trade Hub"),  # Arrived in Seville as part of Spanish trade routes
        (4.4024, 51.2194, "Antwerp - European Distribution"),  # Distributed through Antwerp to northern Europe
        (-0.1276, 51.5074, "London - British Consumption"),  # Consumed in London for textile production
        (104.1954, 35.8617, "China - Global Reach"),  # Reached China as a global commodity
        (35.2433, 38.9637, "Turkey - Global Reach"),  # Also traded in Turkey
        (10.4515, 51.1657, "Germany - European Consumption")  # Distributed widely in Europe
    ],

    "Logwood": [
        (-88.8661, 19.4326, "Yucatan, Mexico - Origin and Production"),  # Logwood was harvested in Yucatan, Mexico
        (-96.1429, 19.1738, "Veracruz - Export Hub"),  # Exported from Veracruz, Mexico
        (-88.7667, 17.5088, "Belize - Collection Point"),  # Collected and exported via Belize
        (-5.9845, 37.3891, "Seville - Spanish Trade Hub"),  # Arrived in Seville for distribution in Europe
        (-0.1276, 51.5074, "London - British Textile Industry"),  # Used in British textile production
        (-71.0589, 42.3601, "Boston - North American Market"),  # Exported to North America, especially Boston
        (-3.7038, 40.4168, "Spain - Consumption and Redistribution"),  # Used and redistributed in Spain
        (-1.1743, 52.3555, "England - Textile Production")  # Final use in England
    ],

    "Brazilwood": [
        (-38.5014, -12.9714, "Salvador, Brazil - Origin and Production"),  # Brazilwood was harvested in Salvador, Brazil
        (-9.1393, 38.7223, "Lisbon - Portuguese Trade Hub"),  # Exported to Lisbon as part of Portuguese trade
        (12.3155, 45.4408, "Venice - Italian Dye Market"),  # Reached Venice for trade in Italy
        (4.4024, 51.2194, "Antwerp - Northern European Distribution"),  # Distributed through Antwerp to Europe
        (-3.7038, 40.4168, "Spain - Spanish Dye Industry"),  # Used in Spain’s dye production
        (-8.2245, 39.3999, "Portugal - Domestic Use and Re-export"),  # Consumed in Portugal and re-exported
        (2.3522, 48.8566, "France - French Dye Industry"),  # Consumed in France
        (4.9041, 52.3676, "Netherlands - Dutch Textile Industry")  # Also distributed in the Netherlands
    ],

    "Annatto": [
        (-89.7244, 21.1619, "Yucatan, Mexico - Origin and Production"),  # Annatto originated in Yucatan
        (-96.1429, 19.1738, "Veracruz - Export Hub"),  # Exported via Veracruz
        (-73.9352, 18.4790, "Caribbean - Production Region"),  # Harvested in the Caribbean
        (-5.9845, 37.3891, "Seville - Spanish Trade Hub"),  # Reached Seville for European distribution
        (-9.1393, 38.7223, "Lisbon - Portuguese Trade Hub"),  # Reached Lisbon as part of Portuguese trade
        (2.3522, 48.8566, "France - French Textile Industry"),  # Used in the French textile industry
        (-0.1276, 51.5074, "England - British Consumption")  # Exported to England for textile production
    ],

    "Safflower": [
        (104.1954, 35.8617, "China - Origin and Production"),  # Safflower was produced in China
        (116.4074, 39.9042, "Beijing - Export Hub"),  # Exported from Beijing
        (78.9629, 20.5937, "India - Production Region"),  # Also produced in India
        (-9.1393, 38.7223, "Lisbon - Portuguese Trade Hub"),  # Exported via Lisbon
        (4.4024, 51.2194, "Antwerp - Distribution to Northern Europe"),  # Distributed via Antwerp
        (12.3155, 45.4408, "Venice - Italian Market"),  # Reached Venice for Italian consumption
        (-3.7038, 40.4168, "Spain - Spanish Textile Industry"),  # Used in Spain’s textile industry
        (2.3522, 48.8566, "France - French Textile Industry"),  # Consumed in France
        (12.4964, 41.9028, "Italy - Italian Textile Industry")  # Used in Italy
    ]
}


# Combine both dye and textile trade routes
combined_trade_routes = {**textile_trade_routes, **dye_trade_routes}

# Combine route colors for both
route_colors = {
    "India to England": 'darkblue',
    "India to Africa": 'green',
    "West Africa to the Americas": 'red',
    "United States to England": 'orange',
    "Mexico to Spain": 'darkred',
    "Peru to Spain": 'darkred',
    "England to Europe": 'purple',
    "France to West Africa": 'yellow',
    "India to China": 'blue',
    "China to Europe": 'lightblue',
    "Caribbean to Spain": 'brown',
    "Brazil to Portugal": 'orange',
    "England to India": 'darkblue',
    "Spain to the Netherlands": 'gold',
    "Indigo": 'darkblue',
    "Cochineal": 'darkred',
    "Logwood": 'purple',
    "Brazilwood": 'orange',
    "Annatto": 'gold',
    "Safflower": 'pink'
}

# Information about key trade routes
combined_route_info = {
    "India to England": 
    "India was one of the world’s largest producers of cotton and indigo, "
    "key raw materials for the British textile industry. The British East India Company monopolized these resources, "
    "exporting them to England to fuel the British Industrial Revolution. This "
    "devastated the local industry. India’s cotton and indigo exports were "
    "essential in sustaining Britain’s dominance in global textile production and trade.",

    "India to Africa": 
    "Indian cotton cloth was exported to Africa as part of the triangular trade, where textiles were exchanged for enslaved "
    "labor. These enslaved Africans were then transported to the Americas to work on plantations. The British used the profits "
    "from selling Indian textiles in Africa to further exploit both African labor and American plantations, creating a system "
    "of economic interdependence that reinforced western dominance.",

    "West Africa to the Americas": 
    "Enslaved Africans were forcibly transported to the Americas, where they worked on cotton and sugar plantations, particularly "
    "in the southern United States and the Caribbean. The labor of these enslaved individuals was crucial to producing the raw cotton "
    "that was then exported to Europe, especially to British textile mills. This system laid the foundation for European wealth and power.",

    "United States to England": 
    "The American South became the primary supplier of raw cotton for Britain. Cotton grown on plantations, "
    "often by enslaved labor, was shipped to England, where it was processed in textile mills in cities like Manchester. This direct "
    "link between American plantations and British factories was vital to the growth of the Industrial Revolution in Britain. The wealth "
    "generated through cotton production strengthened Britain’s global dominance and fueled its empire.",

    "Mexico to Spain": 
    "Mexico, under Spanish colonial rule, became the primary source of cochineal, a valuable red dye made from insects. Cochineal was "
    "harvested by Indigenous laborers and exported to Spain, where it became an essential component of European textiles. The Spanish "
    "monopolized this trade, generating immense wealth. This dye was in high demand in Europe’s textile and fashion industries, and its "
    "production helped solidify Spain’s colonial power.",

    "Peru to Spain": 
    "Peru was a major source of cochineal dye. Under Spanish rule, cochineal was exported from Peru to Spain and was "
    "one of the most valuable dyes in the world at the time. The production of cochineal in Peru further enriched the Spanish Empire, "
    "which dominated global dye trade routes. The wealth derived from this dye trade helped support Spain’s imperial ambitions and the effects of this wealth creation on the economy is still being felt today.",

    "England to Europe": 
    "British textile factories mass-produced finished goods using raw cotton imported from its colonies and the United States. These finished "
    "textiles were then exported across Europe, undercutting local textile production in other countries. British dominance in textile manufacturing "
    "created an economic imbalance, flooding European markets with cheaper British goods and cementing Britain's status as the industrial leader ",

    "France to West Africa": 
    "In addition to British colonial practices, France also leveraged its textile industry to dominate its colonies, especially in West Africa. "
    "French-produced textiles were exported to its African colonies, where they were used as a tool of economic control; by flooding these colonies "
    "with European textiles, France weakened local industries and reinforced its dominance over African economies.",

    "India to China": 
    "India was also a major exporter of indigo to China, which was used in traditional Chinese textiles and crafts. European powers, particularly "
    "the British, acted as intermediaries in this trade. By controlling the flow of indigo between India and China, Europeans not only profited "
    "from the trade but also embelished their influence over Asian markets.",

    "China to Europe": 
    "Chinese silk was highly sought after in Europe, especially in the luxury fashion markets of Paris and London. European merchants "
    "established trade routes to import silk, contributing to Europe’s growing wealth. Silk became a status symbol in European society, "
    "with European powers dominating the trade routes that brought Chinese silk to their markets.",

    "Caribbean to Spain": 
    "Logwood, a key source of black dye, was harvested in the Caribbean and exported to Spain. This dye was essential for the textile industry in "
    "Spain, which relied on vibrant and durable colors for high-quality fabrics. The extraction of logwood from the Caribbean further cemented the "
    "region’s role as a resource for Europe’s growing industries and trade.",

    "Brazil to Portugal": 
    "Brazilwood was one of the most important sources of red dye for European textiles, particularly in Portugal. The extraction of Brazilwood "
    "from the forests of Brazil contributed significantly to the wealth of the Portuguese Empire. Brazilwood’s importance to European textiles "
    "was so great that the country of Brazil itself was named after this valuable export.",

    "England to India": 
    "British-produced textiles, made with cotton imported from its colonies, were exported back to India, devastating local industries. "
    "This colonial system made India dependent on British goods while eroding its own traditional industries. The exploitative nature of this trade "
    "led to widespread economic decline in India and ultimately sparked resistance movements, such as Gandhi’s promotion of khadi (homespun cloth) "
    "as a symbol of self-sufficiency and independence.",

    "Spain to the Netherlands": 
    "Spain, with its colonial dominance over Mexico and Peru, controlled much of the global dye trade. Cochineal and other dyes were exported to the "
    "Netherlands and other European markets, where they were used in high-quality textiles. This trade enriched the Spanish Empire and supported its "
    "imperial ambitions while establishing the Netherlands as a key player in the European textile industry.",
    
    "Indigo": 
    "Indigo, a plant-based dye, was exported from India to Europe, where it was used to create vibrant blue textiles. This trade was controlled by the "
    "British, who exploited India’s natural resources to fuel Europe’s growing demand for indigo-dyed fabrics. Indigo production devastated local farming "
    "communities in India, as British colonial powers enforced strict labor practices to ensure the supply of the dye.",

    "Cochineal": 
    "Cochineal, a red dye made from insects native to Mexico and Peru, was one of the most valuable dyes in European markets. Controlled by the Spanish "
    "Empire, cochineal was harvested by Indigenous laborers and exported to Europe, where it became essential for high-quality textiles and art. The dye "
    "trade enriched Spain and was a cornerstone of its colonial wealth and global influence.",

    "Logwood": 
    "Logwood, extracted from trees in Central America, was used to produce a rich black dye that was highly prized in Europe. This dye was essential for "
    "the production of textiles and clothing, particularly in the Spanish and English textile industries. The logwood trade played a key role in the colonial "
    "exploitation of the Americas by European powers.",

    "Brazilwood": 
    "Brazilwood, exported from Brazil to Portugal, was essential for the production of red dye used in European textiles. The dye trade was so significant "
    "that Brazil was named after this valuable export. Brazilwood extraction fueled the Portuguese economy and was a symbol of the broader exploitation of "
    "natural resources in the Americas for European gain.",

    "Annatto": 
    "Annatto, a natural dye used to produce yellow and orange hues, was harvested in the Caribbean and South America. This dye was used in both textiles and "
    "food coloring and was exported to Europe, where it became an important commodity. The annatto trade linked the Caribbean and South America with European "
    "markets, further reinforcing Europe’s control over global trade routes.",

    "Safflower": 
    "Safflower, used to produce red and pink dyes, was a major export from China and India to Europe. It was particularly important in the production of luxury "
    "silk textiles in European markets. European merchants dominated the trade routes for safflower, reinforcing their control over both Asian markets and the global "
    "textile industry."
}

# Streamlit user interface
st.title("European Dominance Through Textiles, Dyes, and Colonization")
st.write("Explore the historical trade routes that shaped European dominance in the global textile and dye industries during the early modern and industrial eras.")

# Select a trade route
selected_route = st.selectbox("Choose a trade route to display:", list(combined_trade_routes.keys()))

# Plotly globe setup
fig = go.Figure()

# Function to plot a specific trade route
def plot_trade_route(route_name):
    route_coords = combined_trade_routes[route_name]
    color = route_colors[route_name]
    
    for i in range(len(route_coords) - 1):
        lon1, lat1, name1 = route_coords[i]
        lon2, lat2, name2 = route_coords[i + 1]
        
        # Add great circle between points
        fig.add_trace(go.Scattergeo(
            locationmode='ISO-3',
            lon=[lon1, lon2],
            lat=[lat1, lat2],
            mode='lines',
            line=dict(width=2, color=color),
            name=f'{name1} to {name2}'
        ))

    # Add markers for trade stops
    for idx, (lon, lat, name) in enumerate(route_coords):
        # Highlight the first point
        if idx == 0:
            marker_props = dict(size=12, color='red', symbol='circle')  # Highlighted point
        else:
            marker_props = dict(size=8, color=color)
        
        fig.add_trace(go.Scattergeo(
            lon=[lon],
            lat=[lat],
            mode='markers+text',
            text=name,
            textposition="bottom center",
            textfont=dict(color='black'),
            marker=marker_props,
            name=name
        ))

# Plot the selected route
plot_trade_route(selected_route)

# Configure the globe projection and appearance
fig.update_geos(
    projection_type="orthographic",
    showcoastlines=True,
    coastlinecolor="gray",
    showland=True,
    landcolor="lightgreen",
    showocean=True,
    oceancolor="lightblue",
    resolution=50
)

# Update layout
fig.update_layout(
    #title_text=f"Trade Route: {selected_route}",
    margin={"r": 0, "t": 30, "l": 0, "b": 0},
    showlegend=False,
    geo=dict(
        projection_scale=0.85,
        showland=True
    )
)

# Render the Plotly globe in Streamlit
st.plotly_chart(fig, use_container_width=True)

# Display information for the selected route
#st.write(f"**Information for {selected_route}:**")
st.info(combined_route_info[selected_route])
