import 'package:flutter/material.dart';

void main() {
  runApp(ElectroLexApp());
}

class ElectroLexApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ElectroLex',
      theme: ThemeData(
        scaffoldBackgroundColor: Color(0xFFEAF4FF),
        primarySwatch: Colors.blue,
      ),
      home: ElectroLexHome(),
    );
  }
}

class ElectroLexHome extends StatefulWidget {
  @override
  State<ElectroLexHome> createState() => _ElectroLexHomeState();
}

class _ElectroLexHomeState extends State<ElectroLexHome> {
  final TextEditingController _searchController = TextEditingController();
  String _searchQuery = '';

  final List<Map<String, dynamic>> categories = [
    {'title': 'ICs', 'icon': Icons.electrical_services, 'color': Colors.blue},
    {'title': 'Resistors', 'icon': Icons.linear_scale, 'color': Colors.orange},
    {'title': 'Capacitors', 'icon': Icons.battery_charging_full, 'color': Colors.green},
    {'title': 'Diodes', 'icon': Icons.flash_on, 'color': Colors.red},
    {'title': 'Transistors', 'icon': Icons.toggle_on, 'color': Colors.purple},
    {'title': 'LEDs', 'icon': Icons.lightbulb, 'color': Colors.amber},
    {'title': 'Sensors', 'icon': Icons.sensors, 'color': Colors.teal},
    {'title': 'Modules', 'icon': Icons.view_module, 'color': Colors.brown},
    {'title': 'Amplifiers', 'icon': Icons.volume_up, 'color': Colors.blue},
    {'title': 'Switches', 'icon': Icons.toggle_on, 'color': Colors.lightBlue},
    {'title': 'Fuses', 'icon': Icons.power_off, 'color': Colors.redAccent},
    {'title': 'Others', 'icon': Icons.more_horiz, 'color': Colors.grey},

  ];

  final List<Map<String, dynamic>> othersComponents = [
    {'title': 'Amplifiers', 'icon': Icons.volume_up, 'color': Colors.blue},
    {'title': 'Audio Products/Micromotors', 'icon': Icons.headphones, 'color': Colors.pink},
    {'title': 'Circuit Protection', 'icon': Icons.security, 'color': Colors.red},
    {'title': 'Clock and Timing', 'icon': Icons.access_time, 'color': Colors.indigo},
    {'title': 'Connectors', 'icon': Icons.usb, 'color': Colors.teal},
    {'title': 'Crystals/ Oscillators/ Resonators', 'icon': Icons.auto_awesome, 'color': Colors.green},
    {'title': 'Data Converters', 'icon': Icons.swap_horiz, 'color': Colors.orange},
    {'title': 'Development Boards and Tools', 'icon': Icons.developer_board, 'color': Colors.purple},
    {'title': 'Display modules/drivers', 'icon': Icons.display_settings, 'color': Colors.cyan},
    {'title': 'Electrical Appliances', 'icon': Icons.electrical_services, 'color': Colors.grey},
    {'title': 'Electromechanical Components', 'icon': Icons.build_circle, 'color': Colors.blueGrey},
    {'title': 'Embedded Peripheral ICs', 'icon': Icons.memory, 'color': Colors.deepOrange},
    {'title': 'Embedded Controllers', 'icon': Icons.control_camera, 'color': Colors.amber},
    {'title': 'Filters Optimization', 'icon': Icons.tune, 'color': Colors.green},
    {'title': 'Functional Modules', 'icon': Icons.extension, 'color': Colors.lime},
    {'title': 'Fuses', 'icon': Icons.power_off, 'color': Colors.redAccent},
    {'title': 'Hardware/Solders/Batteries', 'icon': Icons.build, 'color': Colors.brown},
    {'title': 'Inductors', 'icon': Icons.all_inclusive, 'color': Colors.indigo},
    {'title': 'Interface ICs', 'icon': Icons.input, 'color': Colors.purpleAccent},
    {'title': 'IoT Communication', 'icon': Icons.wifi, 'color': Colors.tealAccent},
    {'title': 'Logic ICs', 'icon': Icons.memory, 'color': Colors.blueAccent},
    {'title': 'Memory', 'icon': Icons.sd_storage, 'color': Colors.orangeAccent},
    {'title': 'Optoelectronics', 'icon': Icons.light_mode, 'color': Colors.yellow},
    {'title': 'Power Management ICs', 'icon': Icons.battery_full, 'color': Colors.greenAccent},
    {'title': 'Push Button Switch', 'icon': Icons.radio_button_checked, 'color': Colors.deepPurple},
    {'title': 'Relays', 'icon': Icons.flash_auto, 'color': Colors.cyanAccent},
    {'title': 'Rf & Radio', 'icon': Icons.radio, 'color': Colors.red},
    {'title': 'Switches', 'icon': Icons.toggle_on, 'color': Colors.lightBlue},
  ];

  List<Map<String, dynamic>> get allComponents => [...categories, ...othersComponents];

  List<Map<String, dynamic>> get filteredComponents {
    return allComponents
        .where((component) =>
        component['title'].toLowerCase().contains(_searchQuery.toLowerCase()))
        .toList();
  }


  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Scaffold(
        body: SafeArea(
          child: Column(
            children: [
              const SizedBox(height: 32),
              Column(
                children: [
                  Container(
                    width: 64,
                    height: 64,
                    decoration: BoxDecoration(
                      color: Colors.blue,
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Center(
                      child: Text(
                        'EL',
                        style: TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize: 20,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    "ElectroLex",
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.w900,
                      color: Colors.black,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    "Electronics Components Reference Tools",
                    style: TextStyle(
                      fontSize: 14,
                      color: Colors.grey[700],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),
              Container(
                width: 380,
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(25),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black12,
                      blurRadius: 4,
                      offset: Offset(0, 2),
                    ),
                  ],
                ),
                padding: EdgeInsets.all(4),
                child: TabBar(
                  labelColor: Colors.black,
                  unselectedLabelColor: Colors.grey,
                  indicator: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(25),
                  ),
                  indicatorColor: Colors.transparent,
                  indicatorSize: TabBarIndicatorSize.tab,
                  dividerColor: Colors.transparent,
                  tabs: const [
                    Tab(text: 'Home'),
                    Tab(text: 'Search'),
                    Tab(text: 'Settings'),
                  ],
                ),
              ),
              const SizedBox(height: 26),
              Expanded(
                child: TabBarView(
                  children: [
                    _buildHomeTab(context),
                    _buildSearchTab(),
                    const Center(child: Text('Settings Page')),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildHomeTab(BuildContext context) {
    return SingleChildScrollView(
      padding: EdgeInsets.symmetric(horizontal: 16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const SizedBox(height: 24),
          Text("Categories", style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
          const SizedBox(height: 12),
          GridView.count(
            crossAxisCount: 3,
            shrinkWrap: true,
            physics: NeverScrollableScrollPhysics(),
            mainAxisSpacing: 12,
            crossAxisSpacing: 12,
            childAspectRatio: 1,
            children: categories.map((category) {
              return GestureDetector(
                onTap: () {
                  if (category['title'] == 'Others') {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (_) => OthersCategoryPage(othersComponents)),
                    );
                  } else {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (_) => ComponentDetailPage(category['title'])),
                    );
                  }
                },
                child: Container(
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(16),
                    boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 4)],
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Container(
                        width: 48,
                        height: 48,
                        decoration: BoxDecoration(
                          color: category['color'],
                          shape: BoxShape.circle,
                        ),
                        child: Icon(category['icon'], color: Colors.white, size: 28),
                      ),
                      const SizedBox(height: 8),
                      Text(category['title'],
                          style: TextStyle(fontWeight: FontWeight.bold)),
                    ],
                  ),
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }

  Widget _buildSearchTab() {
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: TextField(
            controller: _searchController,
            onChanged: (value) {
              setState(() {
                _searchQuery = value;
              });
            },
            decoration: InputDecoration(
              hintText: 'Search components...',
              prefixIcon: Icon(Icons.search),
              filled: true,
              fillColor: Colors.white,
              contentPadding: EdgeInsets.symmetric(vertical: 0, horizontal: 16),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(30),
                borderSide: BorderSide.none,
              ),
            ),
          ),
        ),
        Expanded(
          child: filteredComponents.isEmpty
              ? Center(child: Text("No components found"))
              : GridView.count(
            crossAxisCount: 3,
            mainAxisSpacing: 12,
            crossAxisSpacing: 12,
            padding: EdgeInsets.all(12),
            childAspectRatio: 1,
            children: filteredComponents.map((item) {
              return GestureDetector(
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (_) => ComponentDetailPage(item['title'])),
                  );
                },
                child: Container(
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(16),
                    boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 4)],
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Container(
                        width: 48,
                        height: 48,
                        decoration: BoxDecoration(
                          color: item['color'],
                          shape: BoxShape.circle,
                        ),
                        child: Icon(item['icon'], color: Colors.white, size: 28),
                      ),
                      const SizedBox(height: 8),
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 6),
                        child: Text(item['title'],
                            textAlign: TextAlign.center,
                            style: TextStyle(
                                fontWeight: FontWeight.bold, fontSize: 12)),
                      ),
                    ],
                  ),
                ),
              );
            }).toList(),
          ),
        ),
      ],
    );
  }
}

class ComponentDetailPage extends StatelessWidget {
  final String title;

  ComponentDetailPage(this.title);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(title)),
      body: Center(
        child: Text('Details about $title', style: TextStyle(fontSize: 18)),
      ),
    );
  }
}

class OthersCategoryPage extends StatelessWidget {
  final List<Map<String, dynamic>> components;

  OthersCategoryPage(this.components);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Others")),
      body: Padding(
        padding: const EdgeInsets.all(12.0),
        child: GridView.count(
          crossAxisCount: 3,
          mainAxisSpacing: 12,
          crossAxisSpacing: 12,
          childAspectRatio: 1,
          children: components.map((item) {
            return GestureDetector(
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                      builder: (_) => ComponentDetailPage(item['title'])),
                );
              },
              child: Container(
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(16),
                  boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 4)],
                ),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 48,
                      height: 48,
                      decoration: BoxDecoration(
                        color: item['color'],
                        shape: BoxShape.circle,
                      ),
                      child: Icon(item['icon'], color: Colors.white, size: 28),
                    ),
                    const SizedBox(height: 8),
                    Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 6),
                      child: Text(item['title'],
                          textAlign: TextAlign.center,
                          style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
                    ),
                  ],
                ),
              ),
            );
          }).toList(),
        ),
      ),
    );
  }
}
