from bas_air_unit_network_dataset.exporters.fpl import (
    Fpl,
    Waypoint as FplWaypoint,
    Route as FplRoute,
    RoutePoint as FplRoutePoint,
)
from bas_air_unit_network_dataset.utils import file_name_with_date
from pathlib import Path

#set some defaults so you can get an output
flightlines = [[(41.60127468451897, -74.88828215007516), (42.59901415, -76.8988384), (39.57415333, -71.01517733), (42.57190242455074, -71.02573286786642)], [(41.57706217418424, -71.02763534528002), (38.57931326, -72.01707906), (37.60417606, -72.90073197), (45.60643677651139, -69.8901749724241)], [(32.611598839202856, -66.89206808484215), (35.60933794, -78.90262583), (33.58447315, -71.01898109), (29.58222188311943, -80.0295381226242)], [(21.58738156303806, -53.03144121052253), (12.58963301, -10.02088343), (43.61449978, -78.90451999), (23.61676086091211, -51.89396149670628)], [(25.62192284367843, -25.89585520877411), (31.61966158, -31.90641445), (86.59479282, -51.02278606), (23.59254119189836, -75.03334458821678)], [(31.597700791742064, -55.03524826646533), (22.5999526, -56.02468899), (23.62482334, -55.9083092), (61.6270847854626, -83.89774921028784)]]


# Create waypoints from flightlines coordinates.  
waypoints = []
for lineno, line in enumerate(flightlines):
    for coordno, coord in enumerate(line):
        waypoint = FplWaypoint()
        #Make sure you map correctly depending on the order of your longitude and latitude values
        waypoint.latitude = coord[0]
        waypoint.longitude = coord[1]
        waypoint.type = "USER WAYPOINT"
        #This is just a string that you can use to identify the waypoint. Mapped to the routepoint identifier later on.
        waypoint.identifier = "Line:" +str(lineno) + "_P:" + str(coordno)
        waypoints.append(waypoint)

# some required values for the library
fpl = Fpl()
route = FplRoute()
route.name = "Air Route"
route.index = 1

# Create route points from waypoints.
for route_waypoint in waypoints:
    route_point = FplRoutePoint()
    route_point.waypoint_identifier = route_waypoint.identifier
    route_point.waypoint_type = "USER WAYPOINT"
    #route_point.waypoint_country_code = "__"
    route.points.append(route_point)

#the fpl object requires waypoints object and a routepoints object
fpl.waypoints = waypoints
fpl.route = route


#output the file to the output directory.  
path=Path("C:\\OutputDir\\FPLdir")
path=path.joinpath(file_name_with_date("00_WAYPOINTS_{{date}}.fpl"))
print(path)
fpl.dump_xml(path)

