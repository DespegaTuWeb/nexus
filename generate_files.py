import os
import json

def save(rel_path, content):
    full_path = os.path.join(os.path.dirname(__file__), rel_path.replace('/', os.sep))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print('Generated:', rel_path)

# --- 0. JSON DATA ---
site_data = {
  "domain": "nexusmotos.com",
  "brandName": "NEXUS MOTOS",
  "importerName": "Grupo Lauzher",
  "importerSlogan": "Principal Importador y Representante Oficial de Nexus en el Perú",
  "mainAddress": "Av. Nicolás Arriola 2278, San Luis, Lima - Perú",
  "centralPhone": "(01) 324-5800",
  "centralMobile": "+51 981 234 567",
  "whatsappNumber": "51981234567",
  "supportEmail": "ventas@nexusmotos.com",
  "hours": "Lunes a Sábado: 8:30 AM - 7:00 PM | Domingos: 9:00 AM - 2:00 PM",
  "ruc": "20512345678",
  "legalDisclaimer": "*Precios referenciales en Soles (S/.) y Dólares Americanos ($ USD) calculados al tipo de cambio referencial. Los precios pueden variar de acuerdo con promociones vigentes, costo de flete interprovincial y disponibilidad de stock en la red de concesionarios autorizados de Grupo Lauzher a nivel nacional. Las imágenes son referenciales y pueden presentar equipamiento opcional."
}
save('src/data/site.json', json.dumps(site_data, indent=2, ensure_ascii=False))

bikes_data = [
  {
    "id": "nexus-250r-hyper",
    "name": "NEXUS 250R HYPER NAKED",
    "slug": "nexus-250r-hyper",
    "category": "pisteras",
    "categoryLabel": "Pisteras y Deportivas",
    "tag": "NUEVO",
    "badge": "TOP 1 VENTAS",
    "year": 2026,
    "priceFromPen": "S/ 8,490*",
    "priceFromUsd": "$ 2,280*",
    "rawPricePen": 8490,
    "installmentsFrom": "S/ 285/mes*",
    "cc": "249.4 cc",
    "power": "24.14 HP / 7500 rpm",
    "torque": "22.5 Nm / 6500 rpm",
    "transmission": "Mecánica 6 velocidades",
    "fuelSystem": "Inyección Electrónica EFI",
    "cooling": "Refrigeración Líquida",
    "brakes": "Doble Disco Ventilado + ABS Opcional",
    "tankCapacity": "14 L (3.7 Gal)",
    "consumption": "135 km/gal",
    "weight": "148 kg",
    "maxSpeed": "135 km/h",
    "colors": [
      { "name": "Negro Mate & Rojo Racing", "hex": "#ef4444" },
      { "name": "Azul Eléctrico & Titanio", "hex": "#2563eb" },
      { "name": "Gris Nardo Grafito", "hex": "#4b5563" }
    ],
    "image": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=1000&q=80",
    "transparentImage": "https://cdn.pixabay.com/photo/2021/01/29/06/21/motorcycle-5960010_1280.png",
    "description": "La naked más imponente del mercado peruano. Diseñada para dominar la pista con aceleración inmediata, chasis multitubular de alta resistencia y suspensión delantera invertida.",
    "highlights": [
      "Tablero 100% digital TFT con indicador de marchas",
      "Iluminación Full LED con DRL frontal agresivo",
      "Suspensión delantera invertida dorada",
      "Monoshock trasero con gas regulable",
      "Escape deportivo en acero inoxidable con sonido grave"
    ],
    "featured": True,
    "showcase": True,
    "comboEligible": True
  },
  {
    "id": "nexus-predator-250",
    "name": "NEXUS PREDATOR 250 GP",
    "slug": "nexus-predator-250",
    "category": "pisteras",
    "categoryLabel": "Pisteras y Deportivas",
    "tag": "RACING",
    "badge": "EDICIÓN ESPECIAL",
    "year": 2026,
    "priceFromPen": "S/ 9,290*",
    "priceFromUsd": "$ 2,490*",
    "rawPricePen": 9290,
    "installmentsFrom": "S/ 315/mes*",
    "cc": "249.0 cc",
    "power": "25.5 HP / 8500 rpm",
    "torque": "23.0 Nm / 7000 rpm",
    "transmission": "Mecánica 6 velocidades con embrague antirrebote",
    "fuelSystem": "Inyección Electrónica Delphi",
    "cooling": "Radiador de Aceite y Aire",
    "brakes": "Doble disco lobulado delantero + Disco posterior",
    "tankCapacity": "15 L",
    "consumption": "130 km/gal",
    "weight": "152 kg",
    "maxSpeed": "145 km/h",
    "colors": [
      { "name": "Rojo GP & Blanco", "hex": "#dc2626" },
      { "name": "Negro Midnight", "hex": "#111827" }
    ],
    "image": "https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1000&q=80",
    "transparentImage": "https://cdn.pixabay.com/photo/2022/04/10/18/39/motorcycle-7124036_1280.png",
    "description": "Carenado aerodinámico integral inspirado en Moto3, cúpula ahumada y postura deportiva pura. El arma definitiva para carretera y asfalto.",
    "highlights": [
      "Carenado integral aerodinámico con tomas de aire",
      "Manillares clip-on para conducción deportiva",
      "Llantas deportivas de compuesto blando",
      "Frenos de alto rendimiento con pinzas radiales"
    ],
    "featured": True,
    "showcase": True,
    "comboEligible": True
  },
  {
    "id": "nexus-dakar-200",
    "name": "NEXUS 200 DAKAR PRO",
    "slug": "nexus-dakar-200",
    "category": "todoterreno",
    "categoryLabel": "Todoterreno y Cross",
    "tag": "TODO TERRENO",
    "badge": "LÍDER RUTAS PERÚ",
    "year": 2026,
    "priceFromPen": "S/ 6,990*",
    "priceFromUsd": "$ 1,880*",
    "rawPricePen": 6990,
    "installmentsFrom": "S/ 235/mes*",
    "cc": "198.5 cc",
    "power": "17.2 HP / 7500 rpm",
    "torque": "16.8 Nm / 6000 rpm",
    "transmission": "Mecánica 5 velocidades",
    "fuelSystem": "Carburador de diafragma de alto torque",
    "cooling": "Aire con aletas disipadoras",
    "brakes": "Disco delantero ondulado + Tambor sellado posterior",
    "tankCapacity": "12 L",
    "consumption": "140 km/gal",
    "weight": "126 kg",
    "maxSpeed": "115 km/h",
    "colors": [
      { "name": "Blanco & Azul Andino", "hex": "#1d4ed8" },
      { "name": "Amarillo Dakar & Negro", "hex": "#eab308" }
    ],
    "image": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=1000&q=80",
    "transparentImage": "https://cdn.pixabay.com/photo/2016/04/07/06/53/bmw-1313343_1280.png",
    "description": "Preparada para los caminos más desafiantes del Perú: sierra, costa y selva. Gran despeje del suelo y suspensión de largo recorrido.",
    "highlights": [
      "Aros de radios reforzados (21 delantera / 18 trasera)",
      "Protector de carter metálico para piedras y barro",
      "Parrilla posterior reforzada lista para alforjas",
      "Escape elevado con protección térmica"
    ],
    "featured": True,
    "showcase": True,
    "comboEligible": True
  },
  {
    "id": "nexus-fox-150",
    "name": "NEXUS 150 FOX URBANA",
    "slug": "nexus-fox-150",
    "category": "urbanas",
    "categoryLabel": "Urbanas y Trabajo",
    "tag": "ECONÓMICA",
    "badge": "165 KM/GALÓN",
    "year": 2026,
    "priceFromPen": "S/ 4,990*",
    "priceFromUsd": "$ 1,340*",
    "rawPricePen": 4990,
    "installmentsFrom": "S/ 175/mes*",
    "cc": "149.2 cc",
    "power": "12.8 HP / 8000 rpm",
    "torque": "11.5 Nm / 6500 rpm",
    "transmission": "Mecánica 5 velocidades",
    "fuelSystem": "Carburador económico de bajo consumo",
    "cooling": "Aire",
    "brakes": "Disco delantero + Tambor trasero",
    "tankCapacity": "13 L",
    "consumption": "165 km/gal",
    "weight": "112 kg",
    "maxSpeed": "105 km/h",
    "colors": [
      { "name": "Rojo Fuego", "hex": "#ef4444" },
      { "name": "Negro Brillante", "hex": "#18181b" },
      { "name": "Azul Noche", "hex": "#1e3a8a" }
    ],
    "image": "https://images.unsplash.com/photo-1609630875171-b1321377ee65?auto=format&fit=crop&w=1000&q=80",
    "transparentImage": "https://cdn.pixabay.com/photo/2018/05/20/19/21/motorcycle-3416550_1280.png",
    "description": "La moto ideal para delivery y trabajo diario en Lima y provincias. Máximo ahorro de combustible, repuestos económicos garantizados por Lauzher.",
    "highlights": [
      "Rendimiento de hasta 165 km por galón",
      "Parrilla espaciosa para baúl de delivery",
      "Puerto de carga USB integrado en timón",
      "Mantenimientos económicos y repuestos inmediatos"
    ],
    "featured": True,
    "showcase": False,
    "comboEligible": True
  },
  {
    "id": "nexus-chacarera-150",
    "name": "NEXUS 150 CHACARERA RÚSTICA",
    "slug": "nexus-chacarera-150",
    "category": "urbanas",
    "categoryLabel": "Urbanas y Trabajo",
    "tag": "FUERZA PURA",
    "badge": "DOBLE AMORTIGUADOR",
    "year": 2026,
    "priceFromPen": "S/ 5,290*",
    "priceFromUsd": "$ 1,420*",
    "rawPricePen": 5290,
    "installmentsFrom": "S/ 185/mes*",
    "cc": "149.0 cc",
    "power": "13.0 HP / 7500 rpm",
    "torque": "12.2 Nm / 6000 rpm",
    "transmission": "Mecánica 5 velocidades con piñón de fuerza",
    "fuelSystem": "Carburador de trabajo pesado",
    "cooling": "Aire",
    "brakes": "Frenos de tambor sellados antipolvo",
    "tankCapacity": "11 L",
    "consumption": "155 km/gal",
    "weight": "118 kg",
    "maxSpeed": "95 km/h",
    "colors": [
      { "name": "Azul Obrero", "hex": "#1d4ed8" },
      { "name": "Rojo Pasión", "hex": "#b91c1c" }
    ],
    "image": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=1000&q=80",
    "transparentImage": "https://cdn.pixabay.com/photo/2021/01/29/06/21/motorcycle-5960010_1280.png",
    "description": "Hecha para la trocha y el campo peruano. Con doble amortiguador trasero y llantas con cocada profunda para traccionar en barro o tierra suelta.",
    "highlights": [
      "Doble amortiguador trasero reforzado de alta carga",
      "Parrilla frontal y posterior de tubos de acero grueso",
      "Chasis reforzado anti-torsión",
      "Faro halógeno redondo de amplio alcance"
    ],
    "featured": False,
    "showcase": False,
    "comboEligible": True
  },
  {
    "id": "nexus-matrix-125",
    "name": "NEXUS MATRIX 125 SCOOTER",
    "slug": "nexus-matrix-125",
    "category": "scooters",
    "categoryLabel": "Scooters Automáticas",
    "tag": "AUTOMÁTICA",
    "badge": "100% CONFORT",
    "year": 2026,
    "priceFromPen": "S/ 4,890*",
    "priceFromUsd": "$ 1,315*",
    "rawPricePen": 4890,
    "installmentsFrom": "S/ 170/mes*",
    "cc": "124.6 cc",
    "power": "9.5 HP / 7500 rpm",
    "torque": "9.0 Nm / 6000 rpm",
    "transmission": "Automática CVT Continua",
    "fuelSystem": "Carburador electrónico",
    "cooling": "Aire forzado por turbina",
    "brakes": "Disco delantero hidráulico + Tambor posterior",
    "tankCapacity": "6 L",
    "consumption": "150 km/gal",
    "weight": "102 kg",
    "maxSpeed": "90 km/h",
    "colors": [
      { "name": "Blanco Glaciar & Gris", "hex": "#f8fafc" },
      { "name": "Gris Grafito Mate", "hex": "#475569" },
      { "name": "Turquesa Urbano", "hex": "#0891b2" }
    ],
    "image": "https://images.unsplash.com/photo-1511994298241-608e28f14fde?auto=format&fit=crop&w=1000&q=80",
    "transparentImage": "https://cdn.pixabay.com/photo/2014/04/03/10/01/vespa-309695_1280.png",
    "description": "Tu movilidad en la ciudad sin cambios de marcha: solo acelera y frena. Espacio bajo el asiento para tu casco y piso plano para compras.",
    "highlights": [
      "Transmisión 100% automática CVT",
      "Maletero interior bajo el asiento",
      "Piso plano con gancho para mochilas y bolsas",
      "Frenos combinados de máxima seguridad"
    ],
    "featured": True,
    "showcase": False,
    "comboEligible": True
  },
  {
    "id": "nexus-titan-250-carga",
    "name": "NEXUS TITAN 250 TRIMOTO CARGA",
    "slug": "nexus-titan-250-carga",
    "category": "trimotos",
    "categoryLabel": "Trimotos de Carga y Pasajeros",
    "tag": "CARGA PESADA",
    "badge": "HASTA 800 KG",
    "year": 2026,
    "priceFromPen": "S/ 11,490*",
    "priceFromUsd": "$ 3,090*",
    "rawPricePen": 11490,
    "installmentsFrom": "S/ 395/mes*",
    "cc": "250.0 cc",
    "power": "18.5 HP / 7000 rpm",
    "torque": "20.0 Nm / 5500 rpm",
    "transmission": "Mecánica 5 velocidades + Marcha Atrás (Reversa)",
    "fuelSystem": "Carburador de alta entrega con bomba",
    "cooling": "Refrigeración Líquida con electroventilador y radiador doble",
    "brakes": "Freno hidráulico en las 3 ruedas",
    "tankCapacity": "16 L",
    "consumption": "85 km/gal",
    "weight": "380 kg",
    "maxSpeed": "75 km/h",
    "colors": [
      { "name": "Azul Industrial", "hex": "#1d4ed8" },
      { "name": "Rojo Carga", "hex": "#dc2626" }
    ],
    "image": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=1000&q=80",
    "transparentImage": "https://cdn.pixabay.com/photo/2016/04/07/06/53/bmw-1313343_1280.png",
    "description": "El socio más productivo para negocios de materiales de construcción, gas, bidones de agua y distribución. Tolva hidráulica de alta resistencia.",
    "highlights": [
      "Capacidad de carga garantizada de 800 kg",
      "Tolva basculante con compuertas abatibles en 3 lados",
      "Corona de fuerza con reductora para pendientes pronunciadas",
      "Refrigeración por radiador con ventilador automático"
    ],
    "featured": True,
    "showcase": False,
    "comboEligible": False
  },
  {
    "id": "nexus-king-200-pasajeros",
    "name": "NEXUS KING 200 TRIMOTO PASAJEROS",
    "slug": "nexus-king-200-pasajeros",
    "category": "trimotos",
    "categoryLabel": "Trimotos de Carga y Pasajeros",
    "tag": "TRANSPORTE",
    "badge": "RENTABILIDAD PURA",
    "year": 2026,
    "priceFromPen": "S/ 12,290*",
    "priceFromUsd": "$ 3,300*",
    "rawPricePen": 12290,
    "installmentsFrom": "S/ 420/mes*",
    "cc": "198.0 cc",
    "power": "15.5 HP / 7500 rpm",
    "torque": "17.2 Nm / 6000 rpm",
    "transmission": "Mecánica 5 velocidades + Reversa",
    "fuelSystem": "Carburador con opción dual GLP / GNV",
    "cooling": "Líquida con radiador",
    "brakes": "Sistema hidráulico con pedal",
    "tankCapacity": "13 L",
    "consumption": "95 km/gal",
    "weight": "340 kg",
    "maxSpeed": "70 km/h",
    "colors": [
      { "name": "Blanco & Azul Línea", "hex": "#0284c7" },
      { "name": "Rojo Urbano", "hex": "#b91c1c" }
    ],
    "image": "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=1000&q=80",
    "transparentImage": "https://cdn.pixabay.com/photo/2021/01/29/06/21/motorcycle-5960010_1280.png",
    "description": "La mototaxi autorizada para transporte público de pasajeros. Cabina cómoda para 3 pasajeros, asientos ergonómicos y chasis reforzado según normas MTC.",
    "highlights": [
      "Estructura reforzada antivuelco aprobada MTC",
      "Asientos traseros de alta densidad para 3 pasajeros",
      "Tablero con velocímetro e indicador de combustible",
      "Lona náutica impermeable con ventanas transparentes de mica reforzada"
    ],
    "featured": False,
    "showcase": False,
    "comboEligible": False
  }
]
save('src/data/bikes.json', json.dumps(bikes_data, indent=2, ensure_ascii=False))

promo_data = {
  "combo": {
    "badge": "OFERTA EXCLUSIVA GRUPO LAUZHER",
    "title": "COMBO MOTERO TODO INCLUIDO",
    "headline": "Sal rodando 100% legal, seguro y equipado desde el día uno",
    "savings": "AHORRA HASTA S/ 1,250 SOLES",
    "bannerImage": "https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1200&q=80",
    "helmetImage": "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=600&q=80",
    "plateBadgeText": "PLACA SUNARP + TARJETA DIGITAL",
    "helmetBadgeText": "CASCO CERTIFICADO DOT",
    "maintenanceBadgeText": "3 MANTENIMIENTOS GRATIS",
    "warrantyBadgeText": "GARANTÍA 12 MESES / 10,000 KM",
    "items": [
      {
        "name": "Moto Nexus 0 Kilómetros",
        "description": "Modelo de tu preferencia con garantía de fábrica respaldada por Grupo Lauzher en todo el país.",
        "icon": "bike",
        "value": "0 KM"
      },
      {
        "name": "Casco Certificado DOT",
        "description": "Casco integral de alta resistencia con visor anti-rayas, protección UV y sistema de ventilación activa.",
        "icon": "shield",
        "value": "VALOR S/ 250"
      },
      {
        "name": "Trámite de Placa y Tarjeta SUNARP",
        "description": "Nosotros hacemos el trámite registral. Te entregamos tu placa física de metal y tu tarjeta de propiedad original.",
        "icon": "file-check",
        "value": "VALOR S/ 450"
      },
      {
        "name": "3 Primeros Mantenimientos Gratuitos",
        "description": "Mano de obra 100% cubierta para los servicios de los 500 km, 1,500 km y 3,000 km en la red de talleres Lauzher.",
        "icon": "wrench",
        "value": "VALOR S/ 350"
      },
      {
        "name": "Kit de Herramientas + Casaca Reflectiva",
        "description": "Herramientas oficiales de emergencia para llevar en tu moto y casaca cortaviento impermeable reflectiva.",
        "icon": "gift",
        "value": "VALOR S/ 200"
      }
    ],
    "terms": "*Promoción válida por tiempo limitado para compras al contado o financiamiento en modelos seleccionados en tiendas oficiales Grupo Lauzher y concesionarios autorizados en todo el Perú."
  },
  "financing": {
    "title": "Crédito Rápido Solo con tu DNI",
    "subtitle": "Evaluación inmediata en menos de 15 minutos",
    "bullets": [
      "Aprobación al instante con DNI (sujeto a evaluación crediticia)",
      "Opciones con 0 Inicial según perfil",
      "Financiamiento desde 12 hasta 36 cuotas fijas en Soles",
      "Aceptamos dependientes, independientes, RUS y RUC 10 o 20"
    ]
  }
}
save('src/data/promotions.json', json.dumps(promo_data, indent=2, ensure_ascii=False))

dealers_data = [
  {
    "id": "central-arriola",
    "name": "Sede Central & Showroom Principal Grupo Lauzher",
    "department": "Lima",
    "city": "Lima",
    "district": "San Luis",
    "address": "Av. Nicolás Arriola 2278, San Luis, Lima",
    "phone": "(01) 324-5800",
    "mobile": "+51 981 234 567",
    "whatsapp": "51981234567",
    "hours": "Lunes a Sábado: 8:30 AM - 7:00 PM | Domingo: 9:00 AM - 2:00 PM",
    "isMain": True,
    "services": ["Showroom Oficial", "Taller Autorizado", "Venta de Repuestos Genuinos", "Asesoría Financiera", "Trámite de Placas SUNARP"]
  },
  {
    "id": "lima-norte-olivos",
    "name": "Concesionario Lauzher Lima Norte",
    "department": "Lima",
    "city": "Lima",
    "district": "Los Olivos",
    "address": "Av. Alfredo Mendiola 3580 (Panamericana Norte), Los Olivos",
    "phone": "(01) 521-4400",
    "mobile": "+51 982 345 678",
    "whatsapp": "51982345678",
    "hours": "Lunes a Sábado: 9:00 AM - 7:00 PM",
    "isMain": False,
    "services": ["Venta de Motos 0km", "Taller Mecánico", "Repuestos"]
  },
  {
    "id": "lima-sur-sjm",
    "name": "Showroom Nexus Lima Sur",
    "department": "Lima",
    "city": "Lima",
    "district": "San Juan de Miraflores",
    "address": "Av. Los Héroes 890, San Juan de Miraflores",
    "phone": "(01) 466-2200",
    "mobile": "+51 983 456 789",
    "whatsapp": "51983456789",
    "hours": "Lunes a Sábado: 9:00 AM - 7:00 PM",
    "isMain": False,
    "services": ["Venta de Motos", "Crédito Directo", "Accesorios"]
  },
  {
    "id": "arequipa-ejercito",
    "name": "Concesionario Lauzher Arequipa",
    "department": "Arequipa",
    "city": "Arequipa",
    "district": "Cerro Colorado",
    "address": "Av. Ejército 714, Cerro Colorado, Arequipa",
    "phone": "(054) 289-450",
    "mobile": "+51 984 567 890",
    "whatsapp": "51984567890",
    "hours": "Lunes a Sábado: 8:30 AM - 6:30 PM",
    "isMain": False,
    "services": ["Showroom", "Taller Especializado", "Almacén de Repuestos"]
  },
  {
    "id": "trujillo-centro",
    "name": "Concesionario Lauzher Trujillo",
    "department": "La Libertad",
    "city": "Trujillo",
    "district": "Trujillo Centro",
    "address": "Av. América Sur 1420, Trujillo",
    "phone": "(044) 223-110",
    "mobile": "+51 985 678 901",
    "whatsapp": "51985678901",
    "hours": "Lunes a Sábado: 9:00 AM - 7:00 PM",
    "isMain": False,
    "services": ["Venta", "Postventa", "Garantía Oficial"]
  },
  {
    "id": "chiclayo-leonardo",
    "name": "Showroom Nexus Chiclayo",
    "department": "Lambayeque",
    "city": "Chiclayo",
    "district": "Chiclayo",
    "address": "Av. José Leonardo Ortiz 540, Chiclayo",
    "phone": "(074) 234-900",
    "mobile": "+51 986 789 012",
    "whatsapp": "51986789012",
    "hours": "Lunes a Sábado: 8:30 AM - 6:30 PM",
    "isMain": False,
    "services": ["Venta 0km", "Financiamiento", "Mantenimiento"]
  },
  {
    "id": "huancayo-castilla",
    "name": "Concesionario Lauzher Huancayo",
    "department": "Junín",
    "city": "Huancayo",
    "district": "El Tambo",
    "address": "Av. Mariscal Castilla 2180, El Tambo, Huancayo",
    "phone": "(064) 245-890",
    "mobile": "+51 987 890 123",
    "whatsapp": "51987890123",
    "hours": "Lunes a Sábado: 8:30 AM - 6:00 PM",
    "isMain": False,
    "services": ["Venta de Motos y Trimotos", "Repuestos para Altura", "Taller"]
  },
  {
    "id": "tarapoto-oriente",
    "name": "Sede Nexus Oriente Tarapoto",
    "department": "San Martín",
    "city": "Tarapoto",
    "district": "Tarapoto",
    "address": "Jr. Jiménez Pimentel 670, Tarapoto",
    "phone": "(042) 522-100",
    "mobile": "+51 988 901 234",
    "whatsapp": "51988901234",
    "hours": "Lunes a Sábado: 8:00 AM - 6:30 PM",
    "isMain": False,
    "services": ["Líder en Motos Chacareras y Trimotos", "Servicio Técnico", "Repuestos"]
  },
  {
    "id": "piura-sanchez",
    "name": "Concesionario Lauzher Piura",
    "department": "Piura",
    "city": "Piura",
    "district": "Piura",
    "address": "Av. Sánchez Cerro 1290, Piura",
    "phone": "(073) 304-200",
    "mobile": "+51 989 012 345",
    "whatsapp": "51989012345",
    "hours": "Lunes a Sábado: 8:30 AM - 6:30 PM",
    "isMain": False,
    "services": ["Venta", "Crédito Inmediato", "Mantenimiento"]
  },
  {
    "id": "cusco-cultura",
    "name": "Concesionario Lauzher Cusco",
    "department": "Cusco",
    "city": "Cusco",
    "district": "Wanchaq",
    "address": "Av. de la Cultura 1520, Wanchaq, Cusco",
    "phone": "(084) 234-567",
    "mobile": "+51 990 123 456",
    "whatsapp": "51990123456",
    "hours": "Lunes a Sábado: 9:00 AM - 6:30 PM",
    "isMain": False,
    "services": ["Venta de Motos", "Taller Autorizado", "Garantía"]
  }
]
save('src/data/dealers.json', json.dumps(dealers_data, indent=2, ensure_ascii=False))

# --- 1. GLOBAL CSS ---

save('src/styles/global.css', '''@import "tailwindcss";

@layer base {
  html {
    scroll-behavior: smooth;
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  }

  body {
    background-color: #0c0e12;
    color: #f3f4f6;
    overflow-x: hidden;
  }
}

.font-display {
  font-family: 'Teko', sans-serif;
}

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: #0f1218;
}

::-webkit-scrollbar-thumb {
  background: #252b36;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #dc2626;
}
''')

# --- 2. LAYOUT ---
save('src/layouts/Layout.astro', '''---
import '../styles/global.css';
import site from '../data/site.json';
import Navbar from '../components/Navbar.astro';
import Footer from '../components/Footer.astro';
import WhatsAppButton from '../components/WhatsAppButton.astro';

interface Props {
  title?: string;
  description?: string;
  image?: string;
  canonicalUrl?: string;
}

const {
  title = "Nexus Motos Perú | Grupo Lauzher - Catálogo Oficial y Financiamiento",
  description = "Nexus Motos en Perú. Principal importador: Grupo Lauzher. Conoce nuestras motos pisteras, urbanas, todoterreno y trimotos. Crédito directo con DNI y Combo Motero con Casco y Placa.",
  image = "/images/og-nexus.jpg",
  canonicalUrl = Astro.url.href,
} = Astro.props;
---

<!doctype html>
<html lang="es" class="scroll-smooth">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="generator" content={Astro.generator} />

    <title>{title}</title>
    <meta name="description" content={description} />
    <link rel="canonical" href={canonicalUrl} />
    <meta name="robots" content="index, follow" />

    <meta property="og:type" content="website" />
    <meta property="og:url" content={canonicalUrl} />
    <meta property="og:title" content={title} />
    <meta property="og:description" content={description} />
    <meta property="og:image" content={image} />
    <meta property="og:site_name" content="Nexus Motos Perú" />

    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content={title} />
    <meta name="twitter:description" content={description} />
    <meta name="twitter:image" content={image} />

    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=Teko:wght@500;600;700&display=swap"
      rel="stylesheet"
    />
  </head>
  <body class="bg-[#0b0d12] text-gray-100 min-h-screen flex flex-col selection:bg-red-600 selection:text-white">
    <Navbar />

    <main class="flex-grow">
      <slot />
    </main>

    <Footer />
    <WhatsAppButton />
  </body>
</html>
''')

# --- 3. NEXUS LOGO ---
save('src/components/NexusLogo.astro', '''---
interface Props {
  className?: string;
  showSubtitle?: boolean;
}

const { className = "h-9", showSubtitle = true } = Astro.props;
---

<a href="/" class={`inline-flex items-center gap-3 select-none group transition-opacity hover:opacity-95 ${className}`}>
  <div class="relative flex items-center justify-center">
    <svg
      viewBox="0 0 120 120"
      class="w-9 h-9 drop-shadow-[0_0_15px_rgba(239,68,68,0.5)] transition-transform duration-300 group-hover:scale-105"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <polygon
        points="60,6 110,32 110,88 60,114 10,88 10,32"
        fill="#12151d"
        stroke="#ef4444"
        stroke-width="5"
      />
      <path
        d="M32 86L32 34L54 34L76 68L76 34L90 34L90 86L68 86L46 52L46 86Z"
        fill="url(#nexus-grad)"
      />
      <polygon
        points="60,6 110,32 60,60"
        fill="#ffffff"
        fill-opacity="0.09"
      />
      <defs>
        <linearGradient id="nexus-grad" x1="32" y1="34" x2="90" y2="86" gradientUnits="userSpaceOnUse">
          <stop stop-color="#ff4343" />
          <stop offset="0.6" stop-color="#ef4444" />
          <stop offset="1" stop-color="#991b1b" />
        </linearGradient>
      </defs>
    </svg>
  </div>

  <div class="flex flex-col leading-none">
    <div class="flex items-baseline gap-1.5">
      <span class="text-3xl font-black tracking-wider uppercase text-white font-['Teko',sans-serif]">
        NEXUS
      </span>
      <span class="text-sm font-bold tracking-widest text-red-500 uppercase font-['Teko',sans-serif]">
        MOTOS
      </span>
    </div>
    {showSubtitle && (
      <div class="flex items-center gap-1 -mt-1">
        <span class="text-[9px] uppercase tracking-wider font-semibold text-gray-400">
          GRUPO <span class="text-red-400 font-bold">LAUZHER</span> PERÚ
        </span>
      </div>
    )}
  </div>
</a>
''')

# --- 4. NAVBAR ---
save('src/components/Navbar.astro', '''---
import NexusLogo from './NexusLogo.astro';
import site from '../data/site.json';

const currentPath = Astro.url.pathname;

const navLinks = [
  { href: '/', label: 'Inicio' },
  { href: '/modelos', label: 'Modelos' },
  { href: '/combos-promociones', label: 'Combo Motero', badge: 'PROMO' },
  { href: '/financiamiento', label: 'Financiamiento' },
  { href: '/concesionarios', label: 'Concesionarios' },
  { href: '/grupo-lauzher', label: 'Grupo Lauzher' },
  { href: '/contacto', label: 'Contacto' },
];
---

<header class="sticky top-0 z-50 w-full transition-all">
  <div class="bg-[#07080b] border-b border-gray-800/80 text-xs text-gray-400 py-1.5 px-4 hidden md:block">
    <div class="max-w-7xl mx-auto flex justify-between items-center">
      <div class="flex items-center gap-6">
        <span class="flex items-center gap-1.5 text-gray-300">
          <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
          <strong class="text-white font-medium">Grupo Lauzher:</strong> Principal Importador Oficial en Perú
        </span>
        <span class="flex items-center gap-1">
          <svg class="w-3.5 h-3.5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          {site.mainAddress}
        </span>
      </div>

      <div class="flex items-center gap-5">
        <a href={`tel:${site.centralPhone.replace(/[^0-9]/g, '')}`} class="hover:text-white transition-colors flex items-center gap-1">
          <svg class="w-3.5 h-3.5 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
          </svg>
          Central: {site.centralPhone}
        </a>
        <a
          href={`https://wa.me/${site.whatsappNumber}?text=Hola%20Nexus%20Motos%20Grupo%20Lauzher,%20deseo%20información`}
          target="_blank"
          rel="noopener noreferrer"
          class="text-emerald-400 hover:text-emerald-300 transition-colors font-medium flex items-center gap-1"
        >
          <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
          WhatsApp Ventas: +51 981 234 567
        </a>
      </div>
    </div>
  </div>

  <nav class="bg-[#0d0f14]/90 backdrop-blur-md border-b border-gray-800/60 px-4 py-3.5">
    <div class="max-w-7xl mx-auto flex items-center justify-between">
      <NexusLogo />

      <div class="hidden lg:flex items-center gap-1 xl:gap-2">
        {navLinks.map((link) => {
          const isActive = currentPath === link.href || (link.href !== '/' && currentPath.startsWith(link.href));
          return (
            <a
              href={link.href}
              class={`relative px-3.5 py-2 text-sm font-semibold uppercase tracking-wider transition-all duration-200 rounded-md ${
                isActive
                  ? 'text-white bg-red-600/15 border-b-2 border-red-500'
                  : 'text-gray-300 hover:text-white hover:bg-white/5'
              }`}
            >
              <span class="flex items-center gap-1.5">
                {link.label}
                {link.badge && (
                  <span class="px-1.5 py-0.5 text-[10px] font-black uppercase rounded bg-red-600 text-white animate-pulse">
                    {link.badge}
                  </span>
                )}
              </span>
            </a>
          );
        })}
      </div>

      <div class="hidden sm:flex items-center gap-3">
        <a
          href="/financiamiento"
          class="px-4 py-2 text-xs font-bold uppercase tracking-wider text-gray-200 border border-gray-700 hover:border-gray-500 hover:bg-gray-800/60 rounded-full transition-all"
        >
          Simular Crédito
        </a>
        <a
          href={`https://wa.me/${site.whatsappNumber}?text=Hola%20Nexus%20Motos,%20deseo%20cotizar%20un%20modelo%20con%20el%20Combo%20Motero`}
          target="_blank"
          rel="noopener noreferrer"
          class="px-5 py-2 text-xs font-bold uppercase tracking-wider text-white bg-red-600 hover:bg-red-700 active:scale-95 rounded-full shadow-lg shadow-red-600/30 transition-all flex items-center gap-1.5"
        >
          <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
          </svg>
          Cotizar Ahora
        </a>
      </div>

      <button
        id="mobile-menu-btn"
        type="button"
        class="lg:hidden p-2 rounded-lg text-gray-400 hover:text-white hover:bg-gray-800 focus:outline-none"
        aria-label="Abrir menú"
      >
        <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>
    </div>
  </nav>

  <div id="mobile-menu" class="hidden lg:hidden bg-[#0a0c10] border-b border-gray-800 px-4 py-5 space-y-3">
    <div class="flex flex-col space-y-1">
      {navLinks.map((link) => (
        <a
          href={link.href}
          class="flex items-center justify-between px-3 py-2.5 text-base font-semibold text-gray-200 hover:bg-gray-800/80 rounded-md"
        >
          <span>{link.label}</span>
          {link.badge && (
            <span class="px-2 py-0.5 text-xs font-bold rounded bg-red-600 text-white">
              {link.badge}
            </span>
          )}
        </a>
      ))}
    </div>

    <div class="pt-4 border-t border-gray-800 space-y-2">
      <a
        href="/financiamiento"
        class="block text-center w-full py-2.5 text-sm font-bold uppercase text-gray-200 border border-gray-700 rounded-lg"
      >
        Simular Financiamiento
      </a>
      <a
        href={`https://wa.me/${site.whatsappNumber}?text=Hola%20Nexus%20Motos,%20deseo%20cotizar`}
        target="_blank"
        rel="noopener noreferrer"
        class="block text-center w-full py-2.5 text-sm font-bold uppercase text-white bg-red-600 rounded-lg shadow-md"
      >
        Cotizar por WhatsApp
      </a>
    </div>
  </div>
</header>

<script>
  const btn = document.getElementById('mobile-menu-btn');
  const menu = document.getElementById('mobile-menu');

  if (btn && menu) {
    btn.addEventListener('click', () => {
      menu.classList.toggle('hidden');
    });
  }
</script>
''')

# --- 5. HERO SLIDER ---
save('src/components/HeroSlider.astro', '''---
import site from '../data/site.json';

const slides = [
  {
    tag: "LANZAMIENTO 2026",
    title: "NUEVA NEXUS 250R HYPER",
    headline: "SIENTE EL LLAMADO DE LA POTENCIA PURA",
    description: "Inyección electrónica EFI, frenos de disco lobulados con ABS y suspensión invertida. La naked definitiva para conquistar el asfalto del Perú.",
    price: "S/ 8,490*",
    installments: "Cuotas desde S/ 285/mes*",
    image: "https://images.unsplash.com/photo-1568772585407-9361f9bf3a87?auto=format&fit=crop&w=1200&q=80",
    link: "/modelos/nexus-250r-hyper",
    primaryCta: "Ver Ficha Técnica",
    accentColor: "from-red-600/30"
  },
  {
    tag: "OFERTA ESTRELLA LAUZHER",
    title: "COMBO MOTERO TODO INCLUIDO",
    headline: "MOTO 0 KM + CASCO + PLACA + MANTENIMIENTOS",
    description: "Llévate tu Nexus equipada para rodar legal hoy mismo. Incluye Casco Certificado DOT, trámite de Placa y Tarjeta ante SUNARP y 3 mantenimientos gratis.",
    price: "Ahorro de S/ 1,250",
    installments: "Aprobación al instante con DNI",
    image: "https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1200&q=80",
    link: "/combos-promociones",
    primaryCta: "Conocer el Combo",
    accentColor: "from-amber-600/30"
  },
  {
    tag: "TODO TERRENO PERÚ",
    title: "NEXUS 200 DAKAR PRO",
    headline: "DESAFÍA CUALQUIER RUTA: COSTA, SIERRA Y SELVA",
    description: "Chasis reforzado, suspensión de largo recorrido, protector de carter de aluminio y torque optimizado para trocha pesada.",
    price: "S/ 6,990*",
    installments: "Desde S/ 235/mes*",
    image: "https://images.unsplash.com/photo-1558981403-c5f9899a28bc?auto=format&fit=crop&w=1200&q=80",
    link: "/modelos/nexus-dakar-200",
    primaryCta: "Explorar Modelo",
    accentColor: "from-blue-600/30"
  }
];
---

<div class="relative w-full h-[620px] md:h-[700px] overflow-hidden bg-black select-none group" id="hero-slider">
  <div class="relative w-full h-full">
    {slides.map((slide, index) => (
      <div
        class={`hero-slide absolute inset-0 transition-opacity duration-1000 ease-in-out ${index === 0 ? 'opacity-100 z-10' : 'opacity-0 z-0 pointer-events-none'}`}
        data-slide-index={index}
      >
        <div class="absolute inset-0">
          <img
            src={slide.image}
            alt={slide.title}
            class="w-full h-full object-cover object-center filter brightness-[0.45] contrast-110 transform scale-105 transition-transform duration-[7000ms] ease-out slide-bg-image"
          />
          <div class="absolute inset-0 bg-gradient-to-t from-[#0b0d12] via-[#0b0d12]/40 to-black/60"></div>
          <div class={`absolute inset-0 bg-gradient-to-r ${slide.accentColor} via-transparent to-black/80`}></div>
        </div>

        <div class="relative z-20 max-w-7xl mx-auto h-full px-6 flex flex-col justify-center">
          <div class="max-w-2xl space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-600/20 border border-red-500/50 backdrop-blur-sm">
              <span class="w-2 h-2 rounded-full bg-red-500 animate-ping"></span>
              <span class="text-xs font-black tracking-widest text-red-400 uppercase font-['Teko',sans-serif]">
                {slide.tag}
              </span>
            </div>

            <h1 class="text-5xl md:text-7xl lg:text-8xl font-black uppercase text-white tracking-tight leading-[0.9] font-['Teko',sans-serif] drop-shadow-lg">
              {slide.title}
            </h1>

            <p class="text-lg md:text-xl font-bold uppercase text-red-500 tracking-wider">
              {slide.headline}
            </p>

            <p class="text-sm md:text-base text-gray-300 leading-relaxed font-normal max-w-xl">
              {slide.description}
            </p>

            <div class="pt-2 flex flex-wrap items-baseline gap-4">
              <div class="flex flex-col">
                <span class="text-xs uppercase text-gray-400 font-semibold tracking-wider">Precio Sugerido</span>
                <span class="text-3xl md:text-4xl font-extrabold text-white tracking-tight font-['Teko',sans-serif]">
                  {slide.price}
                </span>
              </div>
              <div class="h-8 w-[1px] bg-gray-700 hidden sm:block"></div>
              <div class="flex flex-col">
                <span class="text-xs uppercase text-gray-400 font-semibold tracking-wider">Financiamiento</span>
                <span class="text-sm md:text-base font-semibold text-emerald-400">
                  {slide.installments}
                </span>
              </div>
            </div>

            <div class="pt-4 flex flex-wrap items-center gap-4">
              <a
                href={slide.link}
                class="px-8 py-3.5 text-sm font-bold uppercase tracking-wider text-white bg-red-600 hover:bg-red-700 active:scale-95 rounded-full shadow-lg shadow-red-600/40 transition-all flex items-center gap-2"
              >
                {slide.primaryCta}
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
                </svg>
              </a>
              <a
                href={`https://wa.me/${site.whatsappNumber}?text=Hola%20Grupo%20Lauzher,%20deseo%20cotizar%20la%20moto%20${encodeURIComponent(slide.title)}`}
                target="_blank"
                rel="noopener noreferrer"
                class="px-7 py-3.5 text-sm font-bold uppercase tracking-wider text-gray-200 border border-gray-600 hover:border-white hover:bg-white/10 rounded-full transition-all flex items-center gap-2"
              >
                Cotizar por WhatsApp
              </a>
            </div>
          </div>
        </div>
      </div>
    ))}
  </div>

  <button
    id="slider-prev"
    class="absolute left-4 top-1/2 -translate-y-1/2 z-30 w-12 h-12 rounded-full bg-black/50 hover:bg-red-600 border border-white/20 hover:border-red-500 text-white flex items-center justify-center transition-all opacity-80 hover:opacity-100 hover:scale-110 focus:outline-none"
    aria-label="Anterior slide"
  >
    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 19l-7-7 7-7" />
    </svg>
  </button>

  <button
    id="slider-next"
    class="absolute right-4 top-1/2 -translate-y-1/2 z-30 w-12 h-12 rounded-full bg-black/50 hover:bg-red-600 border border-white/20 hover:border-red-500 text-white flex items-center justify-center transition-all opacity-80 hover:opacity-100 hover:scale-110 focus:outline-none"
    aria-label="Siguiente slide"
  >
    <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M9 5l7 7-7 7" />
    </svg>
  </button>

  <div class="absolute bottom-6 left-1/2 -translate-x-1/2 z-30 flex items-center gap-3">
    {slides.map((_, i) => (
      <button
        class={`slider-dot w-3 h-3 rounded-full transition-all duration-300 ${i === 0 ? 'bg-red-600 w-8' : 'bg-white/40 hover:bg-white'}`}
        data-target-slide={i}
        aria-label={`Ir al slide ${i + 1}`}
      ></button>
    ))}
  </div>
</div>

<script>
  let currentSlide = 0;
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.slider-dot');
  const totalSlides = slides.length;
  let autoplayTimer: any = null;

  function showSlide(index: number) {
    slides.forEach((slide, i) => {
      if (i === index) {
        slide.classList.remove('opacity-0', 'pointer-events-none', 'z-0');
        slide.classList.add('opacity-100', 'z-10');
      } else {
        slide.classList.remove('opacity-100', 'z-10');
        slide.classList.add('opacity-0', 'pointer-events-none', 'z-0');
      }
    });

    dots.forEach((dot, i) => {
      if (i === index) {
        dot.classList.add('bg-red-600', 'w-8');
        dot.classList.remove('bg-white/40');
      } else {
        dot.classList.remove('bg-red-600', 'w-8');
        dot.classList.add('bg-white/40');
      }
    });

    currentSlide = index;
  }

  function nextSlide() {
    const next = (currentSlide + 1) % totalSlides;
    showSlide(next);
  }

  function prevSlide() {
    const prev = (currentSlide - 1 + totalSlides) % totalSlides;
    showSlide(prev);
  }

  function startAutoplay() {
    stopAutoplay();
    autoplayTimer = setInterval(nextSlide, 6000);
  }

  function stopAutoplay() {
    if (autoplayTimer) clearInterval(autoplayTimer);
  }

  document.getElementById('slider-next')?.addEventListener('click', () => {
    nextSlide();
    startAutoplay();
  });

  document.getElementById('slider-prev')?.addEventListener('click', () => {
    prevSlide();
    startAutoplay();
  });

  dots.forEach((dot) => {
    dot.addEventListener('click', () => {
      const target = Number(dot.getAttribute('data-target-slide'));
      showSlide(target);
      startAutoplay();
    });
  });

  const slider = document.getElementById('hero-slider');
  slider?.addEventListener('mouseenter', stopAutoplay);
  slider?.addEventListener('mouseleave', startAutoplay);

  startAutoplay();
</script>
''')

# --- 6. BIKE SHOWCASE (Ref 2) ---
save('src/components/BikeShowcase.astro', '''---
import bikes from '../data/bikes.json';

const showcaseBikes = bikes.filter((b) => b.showcase);
---

<section class="py-20 bg-white text-gray-900 overflow-hidden relative" id="showcase-section">
  <div class="absolute inset-0 bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] [background-size:20px_20px] opacity-60"></div>

  <div class="max-w-7xl mx-auto px-6 relative z-10">
    <div class="max-w-3xl mb-8">
      <h2 class="text-5xl md:text-7xl lg:text-8xl font-black uppercase text-gray-900 leading-[0.9] tracking-tight font-['Teko',sans-serif]">
        SIENTE EL LLAMADO DE TU NUEVA MOTO
      </h2>
    </div>

    <div class="relative min-h-[460px] md:min-h-[520px] flex flex-col items-center justify-center">
      <div class="absolute top-2 left-2 md:left-6 flex items-center gap-2 z-20" id="showcase-badges">
        <span class="px-3 py-1 text-xs font-bold uppercase rounded-full bg-amber-400 text-gray-950 shadow-sm" id="badge-tag">
          {showcaseBikes[0].tag}
        </span>
        <span class="px-3 py-1 text-xs font-bold uppercase rounded-full bg-amber-500 text-gray-950 shadow-sm" id="badge-top">
          {showcaseBikes[0].badge}
        </span>
      </div>

      <div class="relative w-full max-w-3xl flex items-center justify-center py-6">
        <img
          id="showcase-bike-img"
          src={showcaseBikes[0].transparentImage}
          alt={showcaseBikes[0].name}
          class="w-full max-w-[620px] h-auto object-contain drop-shadow-[0_28px_30px_rgba(0,0,0,0.35)] transition-all duration-500 transform hover:scale-105"
        />
        <div class="absolute -bottom-2 w-3/4 h-8 bg-black/20 rounded-[100%] blur-md -z-10"></div>
      </div>
    </div>

    <div class="mt-8 max-w-4xl mx-auto">
      <div class="bg-white border border-gray-200 rounded-full shadow-lg p-2 md:p-3 flex items-center justify-between transition-all">
        <button
          id="showcase-prev"
          class="w-12 h-12 md:w-14 md:h-14 rounded-full border border-gray-200 hover:border-gray-900 flex items-center justify-center text-gray-800 hover:text-black hover:bg-gray-100 transition-all focus:outline-none flex-shrink-0 cursor-pointer"
          aria-label="Modelo anterior"
        >
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
        </button>

        <div class="flex-1 grid grid-cols-2 md:grid-cols-4 items-center text-center px-2 md:px-6 divide-x divide-gray-100">
          <div class="px-2 py-1 flex flex-col justify-center">
            <span class="text-xs uppercase text-gray-400 font-bold tracking-wider">Modelo</span>
            <span class="text-xl md:text-2xl font-black text-gray-900 uppercase font-['Teko',sans-serif]" id="spec-name">
              {showcaseBikes[0].name}
            </span>
          </div>

          <div class="px-2 py-1 flex flex-col justify-center">
            <span class="text-xs uppercase text-gray-400 font-bold tracking-wider">Cilindrada</span>
            <span class="text-sm md:text-base font-bold text-gray-900" id="spec-cc">
              {showcaseBikes[0].cc}
            </span>
          </div>

          <div class="px-2 py-1 hidden md:flex flex-col justify-center">
            <span class="text-xs uppercase text-gray-400 font-bold tracking-wider">Potencia</span>
            <span class="text-sm md:text-base font-bold text-gray-900" id="spec-power">
              {showcaseBikes[0].power}
            </span>
          </div>

          <div class="px-2 py-1 hidden md:flex flex-col justify-center">
            <span class="text-xs uppercase text-gray-400 font-bold tracking-wider">Transmisión</span>
            <span class="text-sm md:text-base font-bold text-gray-900 truncate" id="spec-trans">
              {showcaseBikes[0].transmission}
            </span>
          </div>
        </div>

        <button
          id="showcase-next"
          class="w-12 h-12 md:w-14 md:h-14 rounded-full border border-gray-200 hover:border-gray-900 flex items-center justify-center text-gray-800 hover:text-black hover:bg-gray-100 transition-all focus:outline-none flex-shrink-0 cursor-pointer"
          aria-label="Siguiente modelo"
        >
          <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </button>
      </div>

      <div class="mt-6 flex justify-center items-center gap-4">
        <a
          id="showcase-detail-btn"
          href={`/modelos/${showcaseBikes[0].slug}`}
          class="px-6 py-2.5 text-xs font-bold uppercase tracking-wider text-gray-800 border border-gray-300 hover:border-black rounded-full transition-all"
        >
          Ver Ficha Completa
        </a>
        <a
          id="showcase-quote-btn"
          href={`https://wa.me/51981234567?text=Hola%20Grupo%20Lauzher,%20deseo%20cotizar%20la%20moto%20${encodeURIComponent(showcaseBikes[0].name)}`}
          target="_blank"
          rel="noopener noreferrer"
          class="px-6 py-2.5 text-xs font-bold uppercase tracking-wider text-white bg-red-600 hover:bg-red-700 rounded-full shadow-md transition-all flex items-center gap-1.5"
        >
          Cotizar por WhatsApp
        </a>
      </div>
    </div>
  </div>
</section>

<script define:vars={{ showcaseBikes }}>
  let currentIndex = 0;
  const total = showcaseBikes.length;

  const imgEl = document.getElementById('showcase-bike-img');
  const badgeTag = document.getElementById('badge-tag');
  const badgeTop = document.getElementById('badge-top');
  const specName = document.getElementById('spec-name');
  const specCc = document.getElementById('spec-cc');
  const specPower = document.getElementById('spec-power');
  const specTrans = document.getElementById('spec-trans');
  const detailBtn = document.getElementById('showcase-detail-btn');
  const quoteBtn = document.getElementById('showcase-quote-btn');

  function updateShowcase(index) {
    const bike = showcaseBikes[index];

    if (imgEl) {
      imgEl.style.opacity = '0';
      imgEl.style.transform = 'scale(0.95)';

      setTimeout(() => {
        imgEl.src = bike.transparentImage;
        imgEl.alt = bike.name;
        imgEl.style.opacity = '1';
        imgEl.style.transform = 'scale(1)';
      }, 200);
    }

    if (badgeTag) badgeTag.textContent = bike.tag;
    if (badgeTop) badgeTop.textContent = bike.badge;
    if (specName) specName.textContent = bike.name;
    if (specCc) specCc.textContent = bike.cc;
    if (specPower) specPower.textContent = bike.power;
    if (specTrans) specTrans.textContent = bike.transmission;
    if (detailBtn) detailBtn.href = `/modelos/${bike.slug}`;
    if (quoteBtn) {
      quoteBtn.href = `https://wa.me/51981234567?text=Hola%20Grupo%20Lauzher,%20deseo%20cotizar%20la%20moto%20${encodeURIComponent(bike.name)}`;
    }

    currentIndex = index;
  }

  document.getElementById('showcase-next')?.addEventListener('click', () => {
    const next = (currentIndex + 1) % total;
    updateShowcase(next);
  });

  document.getElementById('showcase-prev')?.addEventListener('click', () => {
    const prev = (currentIndex - 1 + total) % total;
    updateShowcase(prev);
  });
</script>
''')

# --- 7. BIKE CAROUSEL (Ref 1) ---
save('src/components/BikeCarousel.astro', '''---
import bikes from '../data/bikes.json';

const categories = [
  { id: 'todas', label: 'Todas' },
  { id: 'pisteras', label: 'Pisteras' },
  { id: 'todoterreno', label: 'Todoterreno' },
  { id: 'urbanas', label: 'Urbanas / Trabajo' },
  { id: 'scooters', label: 'Scooters' },
  { id: 'trimotos', label: 'Trimotos' }
];
---

<section class="py-20 bg-[#fafafa] text-gray-900 border-t border-gray-200" id="catalogo-selector">
  <div class="max-w-7xl mx-auto px-6">
    <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-6 mb-12">
      <div>
        <h2 class="text-4xl md:text-6xl font-black text-gray-900 tracking-tight font-['Teko',sans-serif]">
          ELIGE TU <span class="text-red-600">NUEVA NEXUS</span>
        </h2>
        <p class="text-sm text-gray-500 font-medium">Modelos 2026 con respaldo oficial de Grupo Lauzher en todo el Perú</p>
      </div>

      <div class="flex items-center gap-1.5 overflow-x-auto pb-2 lg:pb-0 scrollbar-none" id="category-tabs">
        {categories.map((cat, i) => (
          <button
            class={`category-filter-btn px-5 py-2.5 rounded-full text-xs md:text-sm font-bold tracking-wider uppercase transition-all duration-200 whitespace-nowrap cursor-pointer ${
              i === 0
                ? 'bg-[#0f1118] text-white shadow-md active-category'
                : 'bg-white text-gray-600 hover:text-black hover:bg-gray-200/80 border border-gray-200/80'
            }`}
            data-category={cat.id}
          >
            {cat.label}
          </button>
        ))}
      </div>
    </div>

    <div class="relative">
      <div
        id="bike-cards-container"
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 transition-all duration-300"
      >
        {bikes.map((bike) => (
          <div
            class="bike-card group bg-[#f3f4f6] hover:bg-white rounded-2xl p-5 border border-transparent hover:border-gray-200 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between"
            data-category={bike.category}
          >
            <div class="relative w-full h-52 flex items-center justify-center p-2 mb-4 overflow-hidden">
              <img
                src={bike.transparentImage}
                alt={bike.name}
                class="max-h-44 w-auto object-contain transition-transform duration-500 group-hover:scale-105 drop-shadow-[0_12px_15px_rgba(0,0,0,0.2)]"
                loading="lazy"
              />
              {bike.tag && (
                <span class="absolute top-2 left-2 px-2 py-0.5 text-[10px] font-black uppercase tracking-wider rounded bg-red-600 text-white">
                  {bike.tag}
                </span>
              )}
            </div>

            <div class="pt-2 border-t border-gray-200/80">
              <h3 class="text-xl font-black text-gray-900 uppercase font-['Teko',sans-serif] tracking-wide group-hover:text-red-600 transition-colors">
                {bike.name}
              </h3>

              <div class="flex items-center justify-between text-xs text-gray-600 font-semibold my-2">
                <span class="flex items-center gap-1">
                  <svg class="w-3.5 h-3.5 text-gray-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                  {bike.year}
                </span>
                <span class="flex items-center gap-1">
                  <svg class="w-3.5 h-3.5 text-gray-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                  </svg>
                  {bike.cc}
                </span>
              </div>

              <div class="mt-3 flex items-center justify-between pt-2 border-t border-gray-200/60">
                <div>
                  <span class="text-[10px] uppercase font-bold text-gray-400 block leading-tight">Desde</span>
                  <span class="text-lg font-black text-gray-900 font-['Teko',sans-serif]">{bike.priceFromPen}</span>
                </div>
                <a
                  href={`/modelos/${bike.slug}`}
                  class="px-3.5 py-1.5 text-xs font-bold uppercase tracking-wider text-gray-900 group-hover:text-white bg-white group-hover:bg-red-600 border border-gray-300 group-hover:border-red-600 rounded-full transition-all"
                >
                  Ver Ficha
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>

    <div class="mt-12 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="w-2.5 h-2.5 rounded-full bg-red-600"></span>
        <span class="w-2 h-2 rounded-full bg-gray-400"></span>
        <span class="w-2 h-2 rounded-full bg-gray-400"></span>
        <span class="w-2 h-2 rounded-full bg-gray-400"></span>
        <span class="w-2 h-2 rounded-full bg-gray-400"></span>
      </div>

      <div class="flex items-center gap-3">
        <a
          href="/modelos"
          class="text-xs font-bold uppercase tracking-wider text-gray-600 hover:text-black mr-2 hidden sm:inline-block"
        >
          Ver todo el catálogo →
        </a>
      </div>
    </div>
  </div>
</section>

<script>
  const filterBtns = document.querySelectorAll('.category-filter-btn');
  const cards = document.querySelectorAll('.bike-card');

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      filterBtns.forEach((b) => {
        b.classList.remove('bg-[#0f1118]', 'text-white', 'shadow-md', 'active-category');
        b.classList.add('bg-white', 'text-gray-600', 'border', 'border-gray-200/80');
      });

      btn.classList.add('bg-[#0f1118]', 'text-white', 'shadow-md', 'active-category');
      btn.classList.remove('bg-white', 'text-gray-600', 'border-gray-200/80');

      const selectedCat = btn.getAttribute('data-category');

      cards.forEach((card) => {
        const cardCat = card.getAttribute('data-category');
        if (selectedCat === 'todas' || cardCat === selectedCat) {
          (card as HTMLElement).style.display = 'flex';
        } else {
          (card as HTMLElement).style.display = 'none';
        }
      });
    });
  });
</script>
''')

# --- 8. COMBO BANNER ---
save('src/components/ComboBanner.astro', '''---
import promotions from '../data/promotions.json';
import site from '../data/site.json';

const combo = promotions.combo;
---

<section class="py-20 bg-gradient-to-b from-[#0b0d12] via-[#121620] to-[#0b0d12] text-white relative overflow-hidden" id="combo-promocion">
  <div class="absolute -top-32 -left-32 w-96 h-96 bg-red-600/20 rounded-full blur-[140px] pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-amber-500/15 rounded-full blur-[140px] pointer-events-none"></div>

  <div class="max-w-7xl mx-auto px-6 relative z-10">
    <div class="text-center max-w-3xl mx-auto mb-14">
      <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-red-600/20 border border-red-500/40 text-red-400 text-xs font-black uppercase tracking-widest font-['Teko',sans-serif] mb-3">
        <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
        {combo.badge}
      </div>
      <h2 class="text-5xl md:text-7xl font-black uppercase tracking-tight font-['Teko',sans-serif] leading-none">
        {combo.title}
      </h2>
      <p class="text-gray-300 text-base md:text-lg font-medium mt-2">
        {combo.headline}
      </p>
      <div class="mt-3 inline-block bg-amber-500/20 border border-amber-500/50 text-amber-300 px-4 py-1.5 rounded-lg text-sm font-bold">
        🎉 {combo.savings}
      </div>
    </div>

    <div class="relative bg-gradient-to-r from-gray-900/90 via-gray-900/60 to-gray-900/90 border border-red-500/30 rounded-3xl p-6 md:p-10 shadow-2xl backdrop-blur-md overflow-hidden">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-7 relative flex items-center justify-center min-h-[340px] md:min-h-[420px]">
          <div class="absolute inset-0 bg-gradient-to-t from-red-600/20 via-transparent to-transparent rounded-2xl"></div>

          <img
            src="https://cdn.pixabay.com/photo/2021/01/29/06/21/motorcycle-5960010_1280.png"
            alt="Moto Nexus Combo"
            class="relative z-10 max-h-72 md:max-h-84 w-auto object-contain drop-shadow-[0_20px_25px_rgba(0,0,0,0.6)] transform hover:scale-105 transition-transform duration-500"
          />

          <div class="absolute top-4 left-2 md:left-6 z-20 bg-gray-950/90 border border-amber-500/40 rounded-2xl p-3 shadow-xl backdrop-blur-md flex items-center gap-3 animate-bounce [animation-duration:3s]">
            <div class="w-10 h-10 rounded-xl bg-amber-500/20 flex items-center justify-center text-amber-400">
              <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <div>
              <span class="text-[10px] uppercase font-bold text-amber-400 block tracking-wider">Incluido Gratis</span>
              <span class="text-xs font-black uppercase text-white font-['Teko',sans-serif] tracking-wide text-sm">CASCO CERTIFICADO DOT</span>
            </div>
          </div>

          <div class="absolute bottom-4 right-2 md:right-6 z-20 bg-gray-950/90 border border-blue-500/40 rounded-2xl p-3 shadow-xl backdrop-blur-md flex items-center gap-3">
            <div class="bg-white text-gray-900 border-2 border-blue-600 rounded px-2.5 py-1 text-center font-mono font-black text-xs shadow-inner">
              <span class="text-[8px] text-blue-700 block tracking-widest font-sans font-bold -mb-1">PERÚ</span>
              7890-NX
            </div>
            <div>
              <span class="text-[10px] uppercase font-bold text-blue-400 block tracking-wider">Gestión 100% Incluida</span>
              <span class="text-xs font-black uppercase text-white font-['Teko',sans-serif] tracking-wide text-sm">PLACA SUNARP + TARJETA</span>
            </div>
          </div>

          <div class="absolute -bottom-2 left-6 z-20 bg-gray-950/80 border border-emerald-500/40 rounded-xl px-3 py-1.5 hidden sm:flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
            <span class="text-xs font-bold text-emerald-400 uppercase">3 Mantenimientos Preventivos</span>
          </div>
        </div>

        <div class="lg:col-span-5 space-y-4">
          <h3 class="text-2xl md:text-3xl font-black uppercase text-white font-['Teko',sans-serif] tracking-wide border-b border-gray-800 pb-2">
            ¿Qué incluye el Combo Motero?
          </h3>

          <div class="space-y-3">
            {combo.items.map((item) => (
              <div class="flex items-start gap-3 bg-white/5 hover:bg-white/10 p-3 rounded-xl border border-gray-800 transition-colors">
                <div class="w-8 h-8 rounded-lg bg-red-600/20 text-red-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
                <div class="flex-1">
                  <div class="flex items-center justify-between">
                    <h4 class="text-sm font-bold text-white">{item.name}</h4>
                    <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-red-950 text-red-300 border border-red-800">
                      {item.value}
                    </span>
                  </div>
                  <p class="text-xs text-gray-400 mt-0.5 leading-relaxed">
                    {item.description}
                  </p>
                </div>
              </div>
            ))}
          </div>

          <div class="pt-4 flex flex-col sm:flex-row gap-3">
            <a
              href={`https://wa.me/${site.whatsappNumber}?text=Hola%20Grupo%20Lauzher,%20deseo%20separar%20el%20Combo%20Motero%20Todo%20Incluido`}
              target="_blank"
              rel="noopener noreferrer"
              class="flex-1 text-center py-3.5 px-6 rounded-full text-xs font-black uppercase tracking-wider text-white bg-red-600 hover:bg-red-700 shadow-lg shadow-red-600/40 transition-all flex items-center justify-center gap-2"
            >
              Separar Mi Combo por WhatsApp
            </a>
            <a
              href="/combos-promociones"
              class="py-3.5 px-6 rounded-full text-xs font-black uppercase tracking-wider text-gray-300 border border-gray-700 hover:border-gray-400 hover:text-white transition-all text-center"
            >
              Más Detalles
            </a>
          </div>

          <p class="text-[10px] text-gray-500 pt-1">
            {combo.terms}
          </p>
        </div>
      </div>
    </div>
  </div>
</section>
''')

# --- 9. FINANCE SIMULATOR ---
save('src/components/FinanceSimulator.astro', '''---
import bikes from '../data/bikes.json';
import site from '../data/site.json';
---

<section class="py-20 bg-[#0e1117] text-white border-t border-gray-800" id="simulador-credito">
  <div class="max-w-7xl mx-auto px-6">
    <div class="text-center max-w-2xl mx-auto mb-12">
      <span class="text-red-500 text-xs font-bold uppercase tracking-widest font-['Teko',sans-serif] text-sm">
        FINANCIAMIENTO INMEDIATO
      </span>
      <h2 class="text-4xl md:text-6xl font-black uppercase tracking-tight font-['Teko',sans-serif] leading-none mt-1">
        CALCULA TU CUOTA EN SOLES
      </h2>
      <p class="text-gray-400 text-sm md:text-base mt-2">
        Evaluación en 15 minutos solo con tu DNI. Aceptamos independientes, dependientes y emprendedores.
      </p>
    </div>

    <div class="max-w-4xl mx-auto bg-gradient-to-b from-[#151922] to-[#10131a] border border-gray-800 rounded-3xl p-6 md:p-10 shadow-2xl">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-7 space-y-6">
          <div>
            <label class="block text-xs uppercase font-bold tracking-wider text-gray-300 mb-2">
              1. Selecciona tu Modelo de Moto
            </label>
            <select
              id="calc-bike-select"
              class="w-full bg-[#0a0c10] border border-gray-700 rounded-xl px-4 py-3.5 text-sm font-semibold text-white focus:outline-none focus:border-red-500 transition-colors"
            >
              {bikes.map((b) => (
                <option value={b.rawPricePen} data-name={b.name} data-image={b.transparentImage}>
                  {b.name} — {b.priceFromPen} ({b.cc})
                </option>
              ))}
            </select>
          </div>

          <div>
            <div class="flex justify-between items-center mb-2">
              <label class="text-xs uppercase font-bold tracking-wider text-gray-300">
                2. Cuota Inicial
              </label>
              <span id="initial-amount-label" class="text-sm font-black text-emerald-400 font-mono">
                S/ 0 (0%)
              </span>
            </div>
            <div class="grid grid-cols-4 gap-2 mb-3">
              <button type="button" class="initial-btn px-3 py-2 text-xs font-bold rounded-lg bg-red-600 text-white border border-red-500 cursor-pointer" data-pct="0">
                0% Inicial
              </button>
              <button type="button" class="initial-btn px-3 py-2 text-xs font-bold rounded-lg bg-gray-800 text-gray-300 border border-gray-700 hover:border-gray-500 cursor-pointer" data-pct="10">
                10%
              </button>
              <button type="button" class="initial-btn px-3 py-2 text-xs font-bold rounded-lg bg-gray-800 text-gray-300 border border-gray-700 hover:border-gray-500 cursor-pointer" data-pct="20">
                20%
              </button>
              <button type="button" class="initial-btn px-3 py-2 text-xs font-bold rounded-lg bg-gray-800 text-gray-300 border border-gray-700 hover:border-gray-500 cursor-pointer" data-pct="30">
                30%
              </button>
            </div>
          </div>

          <div>
            <label class="block text-xs uppercase font-bold tracking-wider text-gray-300 mb-2">
              3. Plazo de Financiamiento
            </label>
            <div class="grid grid-cols-4 gap-2">
              <button type="button" class="term-btn px-3 py-2.5 text-xs font-bold rounded-lg bg-gray-800 text-gray-300 border border-gray-700 hover:border-gray-500 cursor-pointer" data-months="12">
                12 Meses
              </button>
              <button type="button" class="term-btn px-3 py-2.5 text-xs font-bold rounded-lg bg-red-600 text-white border border-red-500 cursor-pointer" data-months="18">
                18 Meses
              </button>
              <button type="button" class="term-btn px-3 py-2.5 text-xs font-bold rounded-lg bg-gray-800 text-gray-300 border border-gray-700 hover:border-gray-500 cursor-pointer" data-months="24">
                24 Meses
              </button>
              <button type="button" class="term-btn px-3 py-2.5 text-xs font-bold rounded-lg bg-gray-800 text-gray-300 border border-gray-700 hover:border-gray-500 cursor-pointer" data-months="36">
                36 Meses
              </button>
            </div>
          </div>
        </div>

        <div class="lg:col-span-5 bg-[#0b0d12] border border-red-500/30 rounded-2xl p-6 text-center flex flex-col justify-between shadow-xl relative overflow-hidden">
          <div class="absolute -top-12 -right-12 w-32 h-32 bg-red-600/10 rounded-full blur-2xl"></div>

          <div>
            <span class="text-xs uppercase font-bold text-gray-400 tracking-wider">Cuota Mensual Estimada</span>
            <div class="my-3">
              <span class="text-5xl md:text-6xl font-black text-red-500 font-['Teko',sans-serif] tracking-tight" id="monthly-installment">
                S/ 295*
              </span>
              <span class="text-xs text-gray-400 block font-medium">al mes (cuota fija en Soles)</span>
            </div>

            <div class="space-y-2 py-3 border-y border-gray-800/80 text-xs text-gray-300">
              <div class="flex justify-between">
                <span class="text-gray-400">Precio de la Moto:</span>
                <span class="font-bold text-white" id="summary-price">S/ 8,490</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-400">Cuota Inicial:</span>
                <span class="font-bold text-emerald-400" id="summary-initial">S/ 0</span>
              </div>
              <div class="flex justify-between">
                <span class="text-gray-400">Plazo Seleccionado:</span>
                <span class="font-bold text-white" id="summary-term">18 meses</span>
              </div>
            </div>
          </div>

          <div class="mt-6 space-y-2">
            <a
              id="whatsapp-credit-btn"
              href={`https://wa.me/${site.whatsappNumber}?text=Hola%20Grupo%20Lauzher,%20deseo%20evaluar%20mi%20crédito%20para%20la%20NEXUS%20250R%20con%200%20inicial`}
              target="_blank"
              rel="noopener noreferrer"
              class="w-full py-3 px-4 rounded-xl text-xs font-black uppercase tracking-wider text-white bg-red-600 hover:bg-red-700 shadow-lg shadow-red-600/40 transition-all flex items-center justify-center gap-2"
            >
              Solicitar Pre-Aprobación con DNI
            </a>
            <p class="text-[9px] text-gray-500">
              *TCEA referencial. Sujeto a evaluación crediticia de la entidad financiera aliada o crédito directo.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  let selectedPrice = 8490;
  let bikeName = 'NEXUS 250R HYPER NAKED';
  let initialPct = 0;
  let selectedMonths = 18;

  const selectEl = document.getElementById('calc-bike-select') as HTMLSelectElement;
  const initialBtns = document.querySelectorAll('.initial-btn');
  const termBtns = document.querySelectorAll('.term-btn');
  const installmentEl = document.getElementById('monthly-installment');
  const initialLabel = document.getElementById('initial-amount-label');
  const summaryPrice = document.getElementById('summary-price');
  const summaryInitial = document.getElementById('summary-initial');
  const summaryTerm = document.getElementById('summary-term');
  const waBtn = document.getElementById('whatsapp-credit-btn') as HTMLAnchorElement;

  function calculate() {
    const initialAmount = Math.round(selectedPrice * (initialPct / 100));
    const amountToFinance = selectedPrice - initialAmount;

    const monthlyRate = 0.019;
    const numerator = monthlyRate * Math.pow(1 + monthlyRate, selectedMonths);
    const denominator = Math.pow(1 + monthlyRate, selectedMonths) - 1;
    const monthlyPayment = Math.round(amountToFinance * (numerator / denominator));

    if (installmentEl) installmentEl.textContent = `S/ ${monthlyPayment}*`;
    if (initialLabel) initialLabel.textContent = `S/ ${initialAmount.toLocaleString()} (${initialPct}%)`;
    if (summaryPrice) summaryPrice.textContent = `S/ ${selectedPrice.toLocaleString()}`;
    if (summaryInitial) summaryInitial.textContent = `S/ ${initialAmount.toLocaleString()}`;
    if (summaryTerm) summaryTerm.textContent = `${selectedMonths} meses`;

    if (waBtn) {
      const msg = `Hola Grupo Lauzher, coticé en la web nexusmotos.com: Modelo: ${bikeName}, Precio S/ ${selectedPrice}, Inicial: S/ ${initialAmount} (${initialPct}%), Plazo: ${selectedMonths} meses con cuota aprox de S/ ${monthlyPayment}. Deseo tramitar mi crédito con DNI.`;
      waBtn.href = `https://wa.me/51981234567?text=${encodeURIComponent(msg)}`;
    }
  }

  selectEl?.addEventListener('change', (e) => {
    const target = e.target as HTMLSelectElement;
    selectedPrice = Number(target.value);
    const selectedOption = target.options[target.selectedIndex];
    bikeName = selectedOption.getAttribute('data-name') || 'Moto Nexus';
    calculate();
  });

  initialBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      initialBtns.forEach((b) => {
        b.classList.remove('bg-red-600', 'text-white', 'border-red-500');
        b.classList.add('bg-gray-800', 'text-gray-300', 'border-gray-700');
      });
      btn.classList.add('bg-red-600', 'text-white', 'border-red-500');
      btn.classList.remove('bg-gray-800', 'text-gray-300', 'border-gray-700');
      initialPct = Number(btn.getAttribute('data-pct'));
      calculate();
    });
  });

  termBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      termBtns.forEach((b) => {
        b.classList.remove('bg-red-600', 'text-white', 'border-red-500');
        b.classList.add('bg-gray-800', 'text-gray-300', 'border-gray-700');
      });
      btn.classList.add('bg-red-600', 'text-white', 'border-red-500');
      btn.classList.remove('bg-gray-800', 'text-gray-300', 'border-gray-700');
      selectedMonths = Number(btn.getAttribute('data-months'));
      calculate();
    });
  });

  calculate();
</script>
''')

# --- 10. LAUZHER GUARANTEE ---
save('src/components/LauzherGuarantee.astro', '''---
const pillars = [
  {
    icon: `<svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" /></svg>`,
    title: "Garantía Oficial de Fábrica",
    desc: "12 meses o 10,000 kilómetros de respaldo directo. Tu inversión está protegida desde el primer día."
  },
  {
    icon: `<svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /></svg>`,
    title: "100% Repuestos Originales",
    desc: "Almacén central en Lima con stock permanente de piezas de motor, carrocería, frenos y electricidad."
  },
  {
    icon: `<svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" /><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" /></svg>`,
    title: "Red Nacional de Talleres",
    desc: "Mecánicos certificados por la marca en Lima, Arequipa, Trujillo, Chiclayo, Huancayo, Tarapoto y más."
  },
  {
    icon: `<svg class="w-7 h-7" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>`,
    title: "Gestoría Registral SUNARP",
    desc: "Entregamos tu moto con placa física y tarjeta de propiedad formal, cumpliendo todas las exigencias de ley."
  }
];
---

<section class="py-20 bg-gradient-to-b from-[#0b0d12] to-[#121620] text-white border-t border-gray-800">
  <div class="max-w-7xl mx-auto px-6">
    <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6 mb-14">
      <div>
        <span class="text-xs font-bold text-red-500 uppercase tracking-widest font-['Teko',sans-serif] text-base">
          IMPORTADOR EXCLUSIVO
        </span>
        <h2 class="text-4xl md:text-6xl font-black uppercase tracking-tight font-['Teko',sans-serif] leading-none mt-1">
          EL RESPALDO DE <span class="text-red-500">GRUPO LAUZHER</span> EN PERÚ
        </h2>
        <p class="text-gray-400 text-sm md:text-base mt-2 max-w-2xl">
          Más de dos décadas importando calidad, tecnología y rendimiento para los moteros peruanos.
        </p>
      </div>

      <a
        href="/grupo-lauzher"
        class="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-red-400 hover:text-red-300 transition-colors"
      >
        Conoce más de Grupo Lauzher →
      </a>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      {pillars.map((pillar) => (
        <div class="bg-[#151922]/80 hover:bg-[#1a202c] border border-gray-800 hover:border-red-500/50 rounded-2xl p-6 transition-all duration-300 group shadow-lg">
          <div class="w-12 h-12 rounded-xl bg-red-600/15 group-hover:bg-red-600 text-red-400 group-hover:text-white flex items-center justify-center transition-colors mb-5">
            <Fragment set:html={pillar.icon} />
          </div>
          <h3 class="text-xl font-bold uppercase text-white font-['Teko',sans-serif] tracking-wide mb-2 group-hover:text-red-400 transition-colors">
            {pillar.title}
          </h3>
          <p class="text-xs text-gray-400 leading-relaxed font-normal">
            {pillar.desc}
          </p>
        </div>
      ))}
    </div>
  </div>
</section>
''')

# --- 11. DEALER LOCATOR ---
save('src/components/DealerLocator.astro', '''---
import dealers from '../data/dealers.json';

const departments = ['Todos', 'Lima', 'Arequipa', 'La Libertad', 'Lambayeque', 'Junín', 'San Martín', 'Piura', 'Cusco'];
---

<section class="py-20 bg-white text-gray-900 border-t border-gray-200" id="red-concesionarios">
  <div class="max-w-7xl mx-auto px-6">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-12">
      <div>
        <span class="text-xs font-bold text-red-600 uppercase tracking-widest font-['Teko',sans-serif] text-base">
          COBERTURA NACIONAL
        </span>
        <h2 class="text-4xl md:text-6xl font-black uppercase tracking-tight font-['Teko',sans-serif] leading-none mt-1">
          RED DE CONCESIONARIOS Y TALLERES
        </h2>
        <p class="text-gray-600 text-sm md:text-base mt-2">
          Encuentra tu punto oficial Nexus más cercano para compra, mantenimiento o repuestos originales.
        </p>
      </div>

      <div class="flex items-center gap-1.5 overflow-x-auto pb-2 scrollbar-none" id="dealer-dept-tabs">
        {departments.map((dept, i) => (
          <button
            class={`dept-btn px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider transition-all cursor-pointer whitespace-nowrap ${
              i === 0
                ? 'bg-gray-900 text-white shadow-sm'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
            }`}
            data-dept={dept}
          >
            {dept}
          </button>
        ))}
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="dealers-grid">
      {dealers.map((dealer) => (
        <div
          class="dealer-card bg-gray-50 border border-gray-200/90 rounded-2xl p-6 hover:shadow-lg transition-all duration-300 flex flex-col justify-between"
          data-department={dealer.department}
        >
          <div>
            <div class="flex items-center justify-between mb-3">
              <span class="px-2.5 py-0.5 text-[10px] font-black uppercase tracking-wider rounded bg-red-100 text-red-700">
                {dealer.department} — {dealer.district}
              </span>
              {dealer.isMain && (
                <span class="px-2 py-0.5 text-[10px] font-bold uppercase rounded bg-gray-900 text-white">
                  SEDE CENTRAL
                </span>
              )}
            </div>

            <h3 class="text-xl font-bold uppercase text-gray-900 font-['Teko',sans-serif] tracking-wide mb-2">
              {dealer.name}
            </h3>

            <div class="space-y-2 text-xs text-gray-600 mb-4">
              <p class="flex items-start gap-2">
                <svg class="w-4 h-4 text-red-600 flex-shrink-0 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
                <span>{dealer.address}</span>
              </p>
              <p class="flex items-center gap-2">
                <svg class="w-4 h-4 text-gray-500 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                </svg>
                <span>{dealer.phone}</span>
              </p>
              <p class="flex items-center gap-2">
                <svg class="w-4 h-4 text-gray-500 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span>{dealer.hours}</span>
              </p>
            </div>

            <div class="flex flex-wrap gap-1 mb-5">
              {dealer.services.map((svc) => (
                <span class="text-[10px] font-semibold bg-gray-200/80 text-gray-700 px-2 py-0.5 rounded">
                  {svc}
                </span>
              ))}
            </div>
          </div>

          <div class="pt-4 border-t border-gray-200 flex items-center gap-3">
            <a
              href={`https://wa.me/${dealer.whatsapp}?text=Hola%20${encodeURIComponent(dealer.name)},%20deseo%20consultar%20sobre%20motos%20Nexus`}
              target="_blank"
              rel="noopener noreferrer"
              class="flex-1 text-center py-2 px-3 text-xs font-bold uppercase rounded-lg text-emerald-700 bg-emerald-100 hover:bg-emerald-200 transition-colors flex items-center justify-center gap-1.5"
            >
              Contactar Sede
            </a>
            <a
              href={`https://maps.google.com/?q=${encodeURIComponent(dealer.address)}`}
              target="_blank"
              rel="noopener noreferrer"
              class="p-2 rounded-lg text-gray-600 hover:text-black hover:bg-gray-200 transition-colors"
              title="Ver en Google Maps"
            >
              <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
              </svg>
            </a>
          </div>
        </div>
      ))}
    </div>
  </div>
</section>

<script>
  const deptBtns = document.querySelectorAll('.dept-btn');
  const dealerCards = document.querySelectorAll('.dealer-card');

  deptBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      deptBtns.forEach((b) => {
        b.classList.remove('bg-gray-900', 'text-white', 'shadow-sm');
        b.classList.add('bg-gray-100', 'text-gray-700');
      });
      btn.classList.add('bg-gray-900', 'text-white', 'shadow-sm');
      btn.classList.remove('bg-gray-100', 'text-gray-700');

      const dept = btn.getAttribute('data-dept');
      dealerCards.forEach((card) => {
        const cardDept = card.getAttribute('data-department');
        if (dept === 'Todos' || cardDept === dept) {
          (card as HTMLElement).style.display = 'flex';
        } else {
          (card as HTMLElement).style.display = 'none';
        }
      });
    });
  });
</script>
''')

# --- 12. WHATSAPP BUTTON ---
save('src/components/WhatsAppButton.astro', '''---
import site from '../data/site.json';
---

<div class="fixed bottom-6 right-6 z-50 flex items-center group">
  <div class="mr-3 hidden md:flex items-center bg-gray-950 text-white border border-gray-800 text-xs font-semibold py-2 px-3 rounded-xl shadow-xl transition-all duration-300 transform group-hover:scale-105 pointer-events-none">
    <span>¿Deseas cotizar tu Nexus? <strong class="text-emerald-400">Escríbenos</strong></span>
  </div>

  <a
    href={`https://wa.me/${site.whatsappNumber}?text=Hola%20Nexus%20Motos%20Grupo%20Lauzher,%20deseo%20asesoría%20sobre%20un%20modelo%20y%20el%20Combo%20Motero`}
    target="_blank"
    rel="noopener noreferrer"
    class="w-14 h-14 rounded-full bg-emerald-500 hover:bg-emerald-600 text-white flex items-center justify-center shadow-[0_10px_25px_rgba(16,185,129,0.45)] hover:shadow-[0_15px_30px_rgba(16,185,129,0.6)] transform hover:scale-110 active:scale-95 transition-all duration-300 relative focus:outline-none"
    aria-label="Contactar por WhatsApp"
  >
    <span class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-red-500 border-2 border-white flex items-center justify-center">
      <span class="w-1.5 h-1.5 rounded-full bg-white animate-ping"></span>
    </span>

    <svg class="w-7 h-7 fill-current" viewBox="0 0 24 24">
      <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.303-.058.116-.087.188-.173.289l-.26.302c-.087.087-.179.182-.077.357.101.174.45 742.968 1.202.666.592 1.229.774 1.403.86.174.087.275.072.376-.044.101-.116.433-.506.549-.68.116-.173.231-.144.39-.087s1.011.477 1.184.564.289.13.332.202c.044.073.044.42-.1.825z" />
    </svg>
  </a>
</div>
''')

# --- 13. FOOTER ---
save('src/components/Footer.astro', '''---
import NexusLogo from './NexusLogo.astro';
import site from '../data/site.json';
---

<footer class="bg-[#07080c] text-gray-400 border-t border-gray-800/80 pt-16 pb-8">
  <div class="max-w-7xl mx-auto px-6">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 mb-12">
      <div class="lg:col-span-2 space-y-4">
        <NexusLogo />
        <p class="text-xs text-gray-400 leading-relaxed max-w-sm pt-2">
          {site.importerSlogan}. Ofrecemos motocicletas pisteras, todoterreno, utilitarias y trimotos de carga con garantía de fábrica, stock nacional de repuestos originales y financiamiento directo.
        </p>

        <div class="bg-white/5 border border-gray-800 rounded-xl p-3.5 space-y-1 text-xs">
          <div class="flex items-center gap-2 text-white font-bold">
            <span class="w-2 h-2 rounded-full bg-red-500"></span>
            Showroom Central & Sede Principal
          </div>
          <p class="text-gray-300">{site.mainAddress}</p>
          <p class="text-gray-400">{site.hours}</p>
        </div>
      </div>

      <div class="space-y-3">
        <h4 class="text-sm font-bold uppercase tracking-wider text-white font-['Teko',sans-serif] text-base">
          Gama de Motos
        </h4>
        <ul class="space-y-2 text-xs">
          <li><a href="/modelos?cat=pisteras" class="hover:text-red-400 transition-colors">Pisteras y Deportivas</a></li>
          <li><a href="/modelos?cat=todoterreno" class="hover:text-red-400 transition-colors">Todoterreno y Cross</a></li>
          <li><a href="/modelos?cat=urbanas" class="hover:text-red-400 transition-colors">Urbanas y de Trabajo</a></li>
          <li><a href="/modelos?cat=scooters" class="hover:text-red-400 transition-colors">Scooters Automáticas</a></li>
          <li><a href="/modelos?cat=trimotos" class="hover:text-red-400 transition-colors">Trimotos de Carga y Pasajeros</a></li>
          <li><a href="/combos-promociones" class="text-red-400 font-bold hover:underline">Combo Motero con Placa</a></li>
        </ul>
      </div>

      <div class="space-y-3">
        <h4 class="text-sm font-bold uppercase tracking-wider text-white font-['Teko',sans-serif] text-base">
          Navegación
        </h4>
        <ul class="space-y-2 text-xs">
          <li><a href="/modelos" class="hover:text-white transition-colors">Catálogo de Modelos</a></li>
          <li><a href="/combos-promociones" class="hover:text-white transition-colors">Promociones y Combos</a></li>
          <li><a href="/financiamiento" class="hover:text-white transition-colors">Simulador de Crédito con DNI</a></li>
          <li><a href="/concesionarios" class="hover:text-white transition-colors">Red de Concesionarios</a></li>
          <li><a href="/grupo-lauzher" class="hover:text-white transition-colors">Sobre Grupo Lauzher</a></li>
          <li><a href="/contacto" class="hover:text-white transition-colors">Atención al Cliente</a></li>
        </ul>
      </div>

      <div class="space-y-4">
        <h4 class="text-sm font-bold uppercase tracking-wider text-white font-['Teko',sans-serif] text-base">
          Atención y Soporte
        </h4>
        <div class="space-y-2 text-xs">
          <p class="text-gray-300">Central: <span class="text-white font-bold">{site.centralPhone}</span></p>
          <p class="text-gray-300">WhatsApp: <span class="text-emerald-400 font-bold">{site.centralMobile}</span></p>
          <p class="text-gray-300">Ventas: <span class="text-white font-medium">{site.supportEmail}</span></p>
        </div>

        <a
          href="/contacto#libro-reclamaciones"
          class="inline-flex items-center gap-3 px-3.5 py-2.5 rounded-xl bg-gray-900 border border-gray-800 hover:border-gray-600 transition-colors group"
        >
          <div class="w-8 h-8 rounded-lg bg-amber-500/10 text-amber-400 flex items-center justify-center">
            <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
            </svg>
          </div>
          <div class="text-left">
            <span class="text-[10px] uppercase font-bold text-gray-400 block">Conforme a Ley</span>
            <span class="text-xs font-bold text-white group-hover:text-amber-400 transition-colors">Libro de Reclamaciones</span>
          </div>
        </a>
      </div>
    </div>

    <div class="py-6 border-t border-gray-800/80 text-[11px] text-gray-500 leading-relaxed">
      <p>{site.legalDisclaimer}</p>
    </div>

    <div class="pt-6 border-t border-gray-800/40 flex flex-col sm:flex-row items-center justify-between text-xs text-gray-500 gap-4">
      <p>© {new Date().getFullYear()} <strong class="text-gray-300">nexusmotos.com</strong> — Marca operada y distribuida por <strong class="text-gray-300">Grupo Lauzher Perú</strong>. Todos los derechos reservados.</p>
      <div class="flex items-center gap-4 text-xs">
        <a href="/contacto" class="hover:text-gray-300 transition-colors">Términos de Garantía</a>
        <span>•</span>
        <a href="/contacto" class="hover:text-gray-300 transition-colors">Política de Privacidad</a>
      </div>
    </div>
  </div>
</footer>
''')

# --- 14. PAGES: INDEX ---
save('src/pages/index.astro', '''---
import Layout from '../layouts/Layout.astro';
import HeroSlider from '../components/HeroSlider.astro';
import BikeShowcase from '../components/BikeShowcase.astro';
import BikeCarousel from '../components/BikeCarousel.astro';
import ComboBanner from '../components/ComboBanner.astro';
import FinanceSimulator from '../components/FinanceSimulator.astro';
import LauzherGuarantee from '../components/LauzherGuarantee.astro';
import DealerLocator from '../components/DealerLocator.astro';
---

<Layout
  title="Nexus Motos Perú | Grupo Lauzher - Web Oficial nexusmotos.com"
  description="Descubre la gama 2026 de Nexus Motos en Perú con el respaldo oficial de Grupo Lauzher. Pisteras, urbanas, todoterreno y trimotos. Combo con Casco y Placa SUNARP y crédito inmediato con DNI."
>
  <HeroSlider />
  <BikeShowcase />
  <BikeCarousel />
  <ComboBanner />
  <FinanceSimulator />
  <LauzherGuarantee />
  <DealerLocator />
</Layout>
''')

# --- 15. PAGES: MODELOS/INDEX ---
save('src/pages/modelos/index.astro', '''---
import Layout from '../../layouts/Layout.astro';
import bikes from '../../data/bikes.json';

const categories = [
  { id: 'todas', label: 'Todos los Modelos' },
  { id: 'pisteras', label: 'Pisteras y Deportivas' },
  { id: 'todoterreno', label: 'Todoterreno y Cross' },
  { id: 'urbanas', label: 'Urbanas y Trabajo' },
  { id: 'scooters', label: 'Scooters Automáticas' },
  { id: 'trimotos', label: 'Trimotos (Carga / Pasajeros)' }
];
---

<Layout
  title="Catálogo Completo de Modelos Nexus Motos 2026 | Grupo Lauzher"
  description="Explora todos los modelos de Nexus Motos en Perú: Pisteras 250cc, Doble propósito 200cc, Scooters 125cc, Urbanas 150cc y Trimotos de carga hasta 800kg."
>
  <section class="bg-gradient-to-b from-black to-[#0f1218] py-16 px-6 border-b border-gray-800">
    <div class="max-w-7xl mx-auto text-center">
      <span class="text-xs font-bold text-red-500 uppercase tracking-widest font-['Teko',sans-serif] text-base">
        LINEUP OFICIAL 2026
      </span>
      <h1 class="text-5xl md:text-7xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight mt-1">
        CATÁLOGO DE MOTOS NEXUS
      </h1>
      <p class="text-gray-400 text-sm md:text-base max-w-2xl mx-auto mt-2">
        Encuentra la moto perfecta para tu estilo de vida o tu negocio, con el respaldo y garantía de Grupo Lauzher en todo el Perú.
      </p>

      <div class="mt-8 flex items-center justify-center gap-2 flex-wrap">
        {categories.map((cat, i) => (
          <button
            class={`catalog-cat-btn px-5 py-2 rounded-full text-xs md:text-sm font-bold uppercase tracking-wider transition-all cursor-pointer ${
              i === 0
                ? 'bg-red-600 text-white shadow-lg shadow-red-600/30'
                : 'bg-white/5 text-gray-300 hover:bg-white/10 border border-gray-800'
            }`}
            data-category={cat.id}
          >
            {cat.label}
          </button>
        ))}
      </div>
    </div>
  </section>

  <section class="py-16 px-6 bg-[#0c0e13]">
    <div class="max-w-7xl mx-auto">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8" id="catalog-grid">
        {bikes.map((bike) => (
          <div
            class="catalog-bike-card bg-[#131720] border border-gray-800/80 hover:border-red-500/50 rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 flex flex-col justify-between group"
            data-category={bike.category}
          >
            <div class="relative bg-gradient-to-b from-[#181d28] to-[#131720] h-64 p-6 flex items-center justify-center overflow-hidden">
              <img
                src={bike.transparentImage}
                alt={bike.name}
                class="max-h-52 w-auto object-contain transition-transform duration-500 group-hover:scale-105 drop-shadow-[0_15px_20px_rgba(0,0,0,0.5)]"
                loading="lazy"
              />

              <div class="absolute top-4 left-4 flex gap-1.5">
                {bike.tag && (
                  <span class="px-2.5 py-0.5 text-[10px] font-black uppercase rounded bg-red-600 text-white tracking-wider">
                    {bike.tag}
                  </span>
                )}
                {bike.badge && (
                  <span class="px-2.5 py-0.5 text-[10px] font-bold uppercase rounded bg-amber-400 text-gray-950">
                    {bike.badge}
                  </span>
                )}
              </div>

              <span class="absolute bottom-3 right-4 text-xs font-bold text-gray-400">
                Año {bike.year}
              </span>
            </div>

            <div class="p-6 flex-1 flex flex-col justify-between space-y-4">
              <div>
                <span class="text-[11px] uppercase font-bold text-red-400 tracking-wider">
                  {bike.categoryLabel}
                </span>
                <h2 class="text-2xl font-black uppercase text-white font-['Teko',sans-serif] tracking-wide mt-0.5 group-hover:text-red-500 transition-colors">
                  {bike.name}
                </h2>
                <p class="text-xs text-gray-400 line-clamp-2 mt-1 leading-relaxed">
                  {bike.description}
                </p>
              </div>

              <div class="grid grid-cols-3 gap-2 py-3 border-y border-gray-800/80 text-center">
                <div class="bg-black/30 rounded-lg p-2">
                  <span class="text-[9px] uppercase font-bold text-gray-500 block">Motor</span>
                  <span class="text-xs font-bold text-gray-200">{bike.cc}</span>
                </div>
                <div class="bg-black/30 rounded-lg p-2">
                  <span class="text-[9px] uppercase font-bold text-gray-500 block">Potencia</span>
                  <span class="text-xs font-bold text-gray-200 truncate">{bike.power.split('/')[0]}</span>
                </div>
                <div class="bg-black/30 rounded-lg p-2">
                  <span class="text-[9px] uppercase font-bold text-gray-500 block">Rendimiento</span>
                  <span class="text-xs font-bold text-gray-200">{bike.consumption}</span>
                </div>
              </div>

              <div class="pt-2 flex items-center justify-between">
                <div>
                  <span class="text-[10px] uppercase font-bold text-gray-400 block">Precio Sugerido</span>
                  <span class="text-2xl font-black text-white font-['Teko',sans-serif] tracking-tight">
                    {bike.priceFromPen}
                  </span>
                </div>

                <div class="flex items-center gap-2">
                  <a
                    href={`/modelos/${bike.slug}`}
                    class="px-4 py-2 text-xs font-bold uppercase tracking-wider text-white bg-red-600 hover:bg-red-700 rounded-full transition-all"
                  >
                    Ficha Técnica
                  </a>
                  <a
                    href={`https://wa.me/51981234567?text=Hola%20Grupo%20Lauzher,%20deseo%20cotizar%20la%20moto%20${encodeURIComponent(bike.name)}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    class="p-2 rounded-full border border-gray-700 hover:border-emerald-500 text-emerald-400 hover:bg-emerald-500/10 transition-all"
                    title="Cotizar por WhatsApp"
                  >
                    <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24">
                      <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.303-.058.116-.087.188-.173.289l-.26.302c-.087.087-.179.182-.077.357.101.174.45 742.968 1.202.666.592 1.229.774 1.403.86.174.087.275.072.376-.044.101-.116.433-.506.549-.68.116-.173.231-.144.39-.087s1.011.477 1.184.564.289.13.332.202c.044.073.044.42-.1.825z" />
                    </svg>
                  </a>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
</Layout>

<script>
  const catBtns = document.querySelectorAll('.catalog-cat-btn');
  const cards = document.querySelectorAll('.catalog-bike-card');

  const urlParams = new URLSearchParams(window.location.search);
  const initialCat = urlParams.get('cat');

  if (initialCat) {
    applyFilter(initialCat);
  }

  catBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const cat = btn.getAttribute('data-category');
      applyFilter(cat);
    });
  });

  function applyFilter(cat: string | null) {
    if (!cat) return;

    catBtns.forEach((b) => {
      if (b.getAttribute('data-category') === cat) {
        b.classList.add('bg-red-600', 'text-white', 'shadow-lg');
        b.classList.remove('bg-white/5', 'text-gray-300');
      } else {
        b.classList.remove('bg-red-600', 'text-white', 'shadow-lg');
        b.classList.add('bg-white/5', 'text-gray-300');
      }
    });

    cards.forEach((card) => {
      const cardCat = card.getAttribute('data-category');
      if (cat === 'todas' || cardCat === cat) {
        (card as HTMLElement).style.display = 'flex';
      } else {
        (card as HTMLElement).style.display = 'none';
      }
    });
  }
</script>
''')

# --- 16. PAGES: MODELOS/[SLUG] ---
save('src/pages/modelos/[slug].astro', '''---
import Layout from '../../layouts/Layout.astro';
import bikes from '../../data/bikes.json';
import site from '../../data/site.json';

export async function getStaticPaths() {
  return bikes.map((bike) => ({
    params: { slug: bike.slug },
    props: { bike },
  }));
}

const { bike } = Astro.props;
const relatedBikes = bikes.filter((b) => b.category === bike.category && b.id !== bike.id).slice(0, 3);
---

<Layout
  title={`${bike.name} 2026 | Ficha Técnica, Precio y Crédito en Perú - Grupo Lauzher`}
  description={`Conoce la nueva ${bike.name} con motor ${bike.cc}, ${bike.power}. Precio desde ${bike.priceFromPen}. Garantía oficial de Grupo Lauzher y facilidades de financiamiento.`}
  image={bike.image}
>
  <div class="bg-[#08090d] border-b border-gray-800 py-3 px-6 text-xs text-gray-400">
    <div class="max-w-7xl mx-auto flex items-center gap-2">
      <a href="/" class="hover:text-white transition-colors">Inicio</a>
      <span>/</span>
      <a href="/modelos" class="hover:text-white transition-colors">Modelos</a>
      <span>/</span>
      <span class="text-red-500 font-semibold">{bike.name}</span>
    </div>
  </div>

  <section class="py-12 md:py-16 px-6 bg-gradient-to-b from-[#0b0d12] via-[#10141d] to-[#0b0d12] text-white">
    <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
      <div class="lg:col-span-7 flex flex-col items-center justify-center relative">
        <div class="w-full flex items-center justify-between mb-4">
          <div class="flex items-center gap-2">
            {bike.tag && (
              <span class="px-3 py-1 text-xs font-black uppercase rounded-full bg-red-600 text-white tracking-wider">
                {bike.tag}
              </span>
            )}
            {bike.badge && (
              <span class="px-3 py-1 text-xs font-bold uppercase rounded-full bg-amber-400 text-gray-950">
                {bike.badge}
              </span>
            )}
          </div>
          <span class="text-sm font-bold text-gray-400 uppercase tracking-widest font-['Teko',sans-serif] text-base">
            Modelo {bike.year}
          </span>
        </div>

        <div class="relative w-full min-h-[340px] md:min-h-[440px] flex items-center justify-center p-6 bg-radial from-red-600/10 via-transparent to-transparent rounded-3xl border border-gray-800/80">
          <img
            id="detail-bike-img"
            src={bike.transparentImage}
            alt={bike.name}
            class="max-h-[380px] w-auto object-contain drop-shadow-[0_25px_30px_rgba(0,0,0,0.6)] transform hover:scale-105 transition-all duration-500"
          />
          <div class="absolute -bottom-2 w-3/4 h-8 bg-black/40 rounded-[100%] blur-md -z-10"></div>
        </div>

        {bike.colors && bike.colors.length > 0 && (
          <div class="mt-6 flex items-center gap-4 bg-white/5 border border-gray-800 rounded-full px-5 py-2.5">
            <span class="text-xs uppercase font-bold text-gray-400 tracking-wider">Colores Disponibles:</span>
            <div class="flex items-center gap-2.5">
              {bike.colors.map((c: any) => (
                <div
                  class="flex items-center gap-1.5 cursor-pointer group"
                  title={c.name}
                >
                  <span
                    class="w-5 h-5 rounded-full border-2 border-white/60 shadow-sm transition-transform group-hover:scale-125"
                    style={`background-color: ${c.hex};`}
                  ></span>
                  <span class="text-[11px] text-gray-300 font-medium hidden sm:inline">{c.name}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>

      <div class="lg:col-span-5 space-y-6">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-red-500 font-['Teko',sans-serif] text-lg">
            {bike.categoryLabel}
          </span>
          <h1 class="text-4xl md:text-6xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight leading-none">
            {bike.name}
          </h1>
          <p class="text-sm text-gray-300 mt-3 leading-relaxed">
            {bike.description}
          </p>
        </div>

        <div class="bg-gradient-to-r from-gray-900 to-[#151922] border border-gray-800 rounded-2xl p-5 space-y-3">
          <div class="flex items-baseline justify-between">
            <div>
              <span class="text-[11px] uppercase font-bold text-gray-400 block">Precio Referencial</span>
              <span class="text-4xl md:text-5xl font-black text-white font-['Teko',sans-serif] tracking-tight text-red-500">
                {bike.priceFromPen}
              </span>
            </div>
            <div class="text-right">
              <span class="text-[11px] uppercase font-bold text-gray-400 block">En Dólares</span>
              <span class="text-2xl font-bold text-gray-300 font-['Teko',sans-serif]">
                {bike.priceFromUsd}
              </span>
            </div>
          </div>

          <div class="pt-3 border-t border-gray-800 flex items-center justify-between text-xs">
            <span class="text-gray-400">Financiamiento sugerido:</span>
            <span class="font-bold text-emerald-400">{bike.installmentsFrom}</span>
          </div>
        </div>

        <div class="space-y-3">
          <a
            href={`https://wa.me/${site.whatsappNumber}?text=Hola%20Grupo%20Lauzher,%20deseo%20cotizar%20la%20moto%20${encodeURIComponent(bike.name)}%20(Precio%20${encodeURIComponent(bike.priceFromPen)})`}
            target="_blank"
            rel="noopener noreferrer"
            class="w-full py-4 px-6 rounded-full text-xs font-black uppercase tracking-wider text-white bg-red-600 hover:bg-red-700 active:scale-95 shadow-xl shadow-red-600/40 transition-all flex items-center justify-center gap-2"
          >
            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.303-.058.116-.087.188-.173.289l-.26.302c-.087.087-.179.182-.077.357.101.174.45 742.968 1.202.666.592 1.229.774 1.403.86.174.087.275.072.376-.044.101-.116.433-.506.549-.68.116-.173.231-.144.39-.087s1.011.477 1.184.564.289.13.332.202c.044.073.044.42-.1.825z" />
            </svg>
            Cotizar por WhatsApp con Asesor
          </a>

          <a
            href="/financiamiento"
            class="w-full py-3.5 px-6 rounded-full text-xs font-black uppercase tracking-wider text-gray-200 border border-gray-700 hover:border-gray-400 hover:bg-white/5 transition-all flex items-center justify-center gap-2 text-center"
          >
            Calcular Cuotas y Financiamiento
          </a>
        </div>

        {bike.comboEligible && (
          <div class="bg-red-950/40 border border-red-500/40 rounded-xl p-4 flex items-center justify-between">
            <div class="space-y-0.5">
              <span class="text-[10px] uppercase font-black tracking-widest text-red-400 block">
                ¡DISPONIBLE EN COMBO MOTERO!
              </span>
              <p class="text-xs text-gray-200 font-medium">
                Llévatela con Casco DOT + Trámite de Placa SUNARP + 3 Mantenimientos.
              </p>
            </div>
            <a
              href="/combos-promociones"
              class="px-3.5 py-1.5 rounded-lg bg-red-600 text-white text-xs font-bold uppercase whitespace-nowrap hover:bg-red-700 transition-colors"
            >
              Ver Combo
            </a>
          </div>
        )}
      </div>
    </div>
  </section>

  <section class="py-16 px-6 bg-[#0c0e13] border-t border-gray-800" id="especificaciones">
    <div class="max-w-5xl mx-auto">
      <div class="text-center mb-12">
        <span class="text-xs font-bold text-red-500 uppercase tracking-widest font-['Teko',sans-serif] text-base">
          INGENIERÍA Y RENDIMIENTO
        </span>
        <h2 class="text-4xl md:text-5xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight">
          FICHA TÉCNICA DETALLADA
        </h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="bg-[#131720] border border-gray-800 rounded-2xl p-6 space-y-4">
          <h3 class="text-xl font-bold uppercase text-red-400 font-['Teko',sans-serif] tracking-wide border-b border-gray-800 pb-2">
            Motor y Prestaciones
          </h3>
          <div class="space-y-2.5 text-xs">
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Cilindrada:</span>
              <span class="text-white font-bold">{bike.cc}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Potencia Máxima:</span>
              <span class="text-white font-bold">{bike.power}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Torque Máximo:</span>
              <span class="text-white font-bold">{bike.torque}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Sistema de Combustible:</span>
              <span class="text-white font-bold">{bike.fuelSystem}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Refrigeración:</span>
              <span class="text-white font-bold">{bike.cooling}</span>
            </div>
            <div class="flex justify-between py-1">
              <span class="text-gray-400 font-medium">Velocidad Máxima Aprox:</span>
              <span class="text-white font-bold">{bike.maxSpeed}</span>
            </div>
          </div>
        </div>

        <div class="bg-[#131720] border border-gray-800 rounded-2xl p-6 space-y-4">
          <h3 class="text-xl font-bold uppercase text-red-400 font-['Teko',sans-serif] tracking-wide border-b border-gray-800 pb-2">
            Chasis, Frenos y Autonomía
          </h3>
          <div class="space-y-2.5 text-xs">
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Transmisión:</span>
              <span class="text-white font-bold">{bike.transmission}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Sistema de Frenos:</span>
              <span class="text-white font-bold">{bike.brakes}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Capacidad de Tanque:</span>
              <span class="text-white font-bold">{bike.tankCapacity}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Consumo Estimado:</span>
              <span class="text-white font-bold">{bike.consumption}</span>
            </div>
            <div class="flex justify-between py-1 border-b border-gray-800/50">
              <span class="text-gray-400 font-medium">Peso en Seco:</span>
              <span class="text-white font-bold">{bike.weight}</span>
            </div>
            <div class="flex justify-between py-1">
              <span class="text-gray-400 font-medium">Garantía Oficial:</span>
              <span class="text-emerald-400 font-bold">12 Meses o 10,000 km (Grupo Lauzher)</span>
            </div>
          </div>
        </div>
      </div>

      {bike.highlights && (
        <div class="mt-8 bg-[#131720] border border-gray-800 rounded-2xl p-6">
          <h3 class="text-xl font-bold uppercase text-white font-['Teko',sans-serif] tracking-wide mb-4">
            Equipamiento Destacado
          </h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {bike.highlights.map((h: string) => (
              <div class="flex items-center gap-2 text-xs text-gray-300">
                <svg class="w-4 h-4 text-red-500 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7" />
                </svg>
                <span>{h}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  </section>

  {relatedBikes.length > 0 && (
    <section class="py-16 px-6 bg-black border-t border-gray-800">
      <div class="max-w-7xl mx-auto">
        <h2 class="text-3xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight mb-8">
          Modelos Relacionados
        </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {relatedBikes.map((rel) => (
            <a
              href={`/modelos/${rel.slug}`}
              class="bg-[#12151c] hover:bg-[#181d27] border border-gray-800 rounded-2xl p-5 transition-all group flex flex-col justify-between"
            >
              <div class="h-44 flex items-center justify-center p-2">
                <img
                  src={rel.transparentImage}
                  alt={rel.name}
                  class="max-h-36 w-auto object-contain transition-transform group-hover:scale-105"
                  loading="lazy"
                />
              </div>
              <div class="pt-3 border-t border-gray-800 flex items-center justify-between">
                <div>
                  <h3 class="text-lg font-black uppercase text-white font-['Teko',sans-serif]">
                    {rel.name}
                  </h3>
                  <span class="text-xs text-gray-400 font-medium">{rel.cc}</span>
                </div>
                <span class="text-red-500 font-bold text-sm">{rel.priceFromPen}</span>
              </div>
            </a>
          ))}
        </div>
      </div>
    </section>
  )}
</Layout>
''')

# --- 17. PAGES: COMBOS-PROMOCIONES ---
save('src/pages/combos-promociones.astro', '''---
import Layout from '../layouts/Layout.astro';
import promotions from '../data/promotions.json';
import bikes from '../data/bikes.json';
import site from '../data/site.json';

const combo = promotions.combo;
const eligibleBikes = bikes.filter((b) => b.comboEligible);
---

<Layout
  title="Combo Motero Todo Incluido: Moto 0km + Casco DOT + Placa SUNARP | Grupo Lauzher"
  description="Lleva tu moto Nexus equipada desde el primer día: Casco Certificado DOT, placa física SUNARP, tarjeta de propiedad y 3 mantenimientos gratis. Ahorra hasta S/ 1,250 Soles."
>
  <section class="bg-gradient-to-b from-black via-[#141824] to-[#0b0d12] py-20 px-6 border-b border-gray-800 relative overflow-hidden">
    <div class="absolute -top-24 -left-24 w-96 h-96 bg-red-600/20 rounded-full blur-[120px]"></div>
    <div class="max-w-7xl mx-auto text-center relative z-10">
      <span class="inline-block px-4 py-1 rounded-full bg-red-600/20 border border-red-500/40 text-red-400 text-xs font-black uppercase tracking-widest font-['Teko',sans-serif] mb-3">
        {combo.badge}
      </span>
      <h1 class="text-5xl md:text-7xl lg:text-8xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight leading-none">
        {combo.title}
      </h1>
      <p class="text-xl md:text-2xl font-bold uppercase text-amber-400 tracking-wide mt-2">
        {combo.headline}
      </p>
      <div class="mt-4 inline-block bg-amber-400 text-gray-950 font-black px-6 py-2 rounded-xl text-base tracking-wider uppercase shadow-xl font-['Teko',sans-serif] text-xl">
        🎉 {combo.savings}
      </div>
    </div>
  </section>

  <section class="py-16 px-6 bg-[#0c0e14]">
    <div class="max-w-5xl mx-auto space-y-12">
      <div class="text-center">
        <h2 class="text-3xl md:text-5xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight">
          TODO LO QUE VIENE EN TU PACK
        </h2>
        <p class="text-gray-400 text-sm mt-1">
          Sin costos ocultos, sin sorpresas. Sal rodando de la tienda 100% legal.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        {combo.items.map((item, idx) => (
          <div class="bg-[#141822] border border-gray-800 rounded-2xl p-6 flex items-start gap-4 hover:border-red-500/40 transition-colors">
            <div class="w-12 h-12 rounded-xl bg-red-600/20 text-red-500 flex items-center justify-center font-bold text-lg flex-shrink-0 font-['Teko',sans-serif] text-2xl">
              0{idx + 1}
            </div>
            <div class="space-y-1 flex-1">
              <div class="flex items-center justify-between">
                <h3 class="text-lg font-bold text-white uppercase font-['Teko',sans-serif] tracking-wide">
                  {item.name}
                </h3>
                <span class="text-[10px] font-black uppercase px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/30">
                  {item.value}
                </span>
              </div>
              <p class="text-xs text-gray-400 leading-relaxed">
                {item.description}
              </p>
            </div>
          </div>
        ))}
      </div>

      <div class="bg-white/5 border border-gray-800 rounded-2xl p-6 text-xs text-gray-400 leading-relaxed">
        <h4 class="font-bold text-white uppercase mb-1">Términos y Condiciones de la Campaña:</h4>
        <p>{combo.terms}</p>
      </div>
    </div>
  </section>

  <section class="py-16 px-6 bg-[#090b0f] border-t border-gray-800">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-12">
        <h2 class="text-4xl md:text-6xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight">
          ELIGE TU MOTO PARA APLICAR EL COMBO
        </h2>
        <p class="text-gray-400 text-sm">
          Aplica tanto para compras al contado como financiamiento en cuotas mensuales.
        </p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {eligibleBikes.map((bike) => (
          <div class="bg-[#121620] border border-gray-800 rounded-2xl p-6 flex flex-col justify-between group hover:border-red-500/50 transition-all shadow-lg">
            <div class="h-48 flex items-center justify-center p-2 mb-4">
              <img
                src={bike.transparentImage}
                alt={bike.name}
                class="max-h-40 w-auto object-contain transition-transform group-hover:scale-105 drop-shadow-[0_15px_20px_rgba(0,0,0,0.5)]"
                loading="lazy"
              />
            </div>

            <div class="space-y-3">
              <div>
                <span class="text-[10px] font-bold text-red-400 uppercase tracking-wider">{bike.categoryLabel}</span>
                <h3 class="text-2xl font-black uppercase text-white font-['Teko',sans-serif]">{bike.name}</h3>
                <span class="text-sm font-semibold text-gray-400">{bike.cc} • Año {bike.year}</span>
              </div>

              <div class="pt-3 border-t border-gray-800 flex items-center justify-between">
                <div>
                  <span class="text-[10px] text-gray-400 uppercase block font-semibold">Precio Moto</span>
                  <span class="text-2xl font-black text-white font-['Teko',sans-serif]">{bike.priceFromPen}</span>
                </div>
                <a
                  href={`https://wa.me/${site.whatsappNumber}?text=Hola%20Grupo%20Lauzher,%20deseo%20separar%20el%20Combo%20Motero%20con%20la%20${encodeURIComponent(bike.name)}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  class="px-4 py-2 rounded-full text-xs font-bold uppercase tracking-wider bg-red-600 hover:bg-red-700 text-white shadow-md transition-all flex items-center gap-1.5"
                >
                  Separar Combo
                </a>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  </section>
</Layout>
''')

# --- 18. PAGES: FINANCIAMIENTO ---
save('src/pages/financiamiento.astro', '''---
import Layout from '../layouts/Layout.astro';
import FinanceSimulator from '../components/FinanceSimulator.astro';
import promotions from '../data/promotions.json';
import site from '../data/site.json';

const fin = promotions.financing;
---

<Layout
  title="Financiamiento y Crédito de Motos en Perú | Solo con DNI - Grupo Lauzher"
  description="Financia tu moto Nexus en cuotas fijas en Soles. Evaluación en 15 minutos solo con DNI. Opciones con 0 Inicial para independientes y dependientes con Grupo Lauzher."
>
  <section class="bg-gradient-to-b from-black via-[#11151e] to-[#0c0e13] py-20 px-6 border-b border-gray-800 text-center">
    <div class="max-w-4xl mx-auto space-y-3">
      <span class="text-xs font-bold text-red-500 uppercase tracking-widest font-['Teko',sans-serif] text-base">
        CRÉDITO FÁCIL Y SEGURO
      </span>
      <h1 class="text-5xl md:text-7xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight leading-none">
        FINANCIA TU MOTO NEXUS
      </h1>
      <p class="text-gray-300 text-base md:text-lg max-w-2xl mx-auto">
        Obtén tu moto 0 km hoy mismo sin complicaciones. Evaluamos tu crédito en menos de 15 minutos solo con tu documento de identidad.
      </p>
    </div>
  </section>

  <FinanceSimulator />

  <section class="py-20 px-6 bg-[#090b10] border-t border-gray-800">
    <div class="max-w-7xl mx-auto">
      <div class="text-center mb-14">
        <h2 class="text-4xl md:text-5xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight">
          REQUISITOS SIMPLES PARA CALIFICAR
        </h2>
        <p class="text-gray-400 text-sm">
          Planes flexibles pensados para la realidad laboral de los peruanos.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-[#131722] border border-gray-800 rounded-2xl p-6 space-y-3">
          <div class="w-10 h-10 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center font-bold">
            01
          </div>
          <h3 class="text-2xl font-bold uppercase text-white font-['Teko',sans-serif]">Trabajadores en Planilla</h3>
          <ul class="space-y-2 text-xs text-gray-400">
            <li>✔ Copia de DNI vigente</li>
            <li>✔ Últimas 3 boletas de pago</li>
            <li>✔ Recibo de agua o luz de domicilio</li>
            <li>✔ Buen historial en Infocorp / Sentinel</li>
          </ul>
        </div>

        <div class="bg-[#131722] border border-gray-800 rounded-2xl p-6 space-y-3">
          <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center font-bold">
            02
          </div>
          <h3 class="text-2xl font-bold uppercase text-white font-['Teko',sans-serif]">Independientes y RUS</h3>
          <ul class="space-y-2 text-xs text-gray-400">
            <li>✔ DNI vigente</li>
            <li>✔ Ficha RUC (RUS, RUC 10 o RUC 20)</li>
            <li>✔ Últimos 3 pagos a la SUNAT o recibos por honorarios</li>
            <li>✔ Movimientos de cuenta o fotos del negocio</li>
          </ul>
        </div>

        <div class="bg-[#131722] border border-gray-800 rounded-2xl p-6 space-y-3">
          <div class="w-10 h-10 rounded-xl bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold">
            03
          </div>
          <h3 class="text-2xl font-bold uppercase text-white font-['Teko',sans-serif]">Delivery y Emprendedores</h3>
          <ul class="space-y-2 text-xs text-gray-400">
            <li>✔ DNI vigente</li>
            <li>✔ Capturas de ingresos de apps (PedidosYa, Rappi, Uber)</li>
            <li>✔ Recibo de servicio de vivienda</li>
            <li>✔ Evaluación ágil con entidades aliadas</li>
          </ul>
        </div>
      </div>

      <div class="mt-16 bg-[#151924] border border-gray-800 rounded-2xl p-8 text-center space-y-4">
        <h3 class="text-xl font-bold uppercase text-white font-['Teko',sans-serif] tracking-wider">
          ENTIDADES FINANCIERAS ALIADAS
        </h3>
        <p class="text-xs text-gray-400 max-w-xl mx-auto">
          Grupo Lauzher trabaja en alianza con las principales entidades de crédito vehicular y microfinanzas del país:
        </p>
        <div class="flex flex-wrap items-center justify-center gap-6 pt-2">
          <span class="px-5 py-2.5 rounded-xl bg-black/40 border border-gray-700 text-xs font-bold text-gray-200">
            Santander Consumer
          </span>
          <span class="px-5 py-2.5 rounded-xl bg-black/40 border border-gray-700 text-xs font-bold text-gray-200">
            Caja Huancayo
          </span>
          <span class="px-5 py-2.5 rounded-xl bg-black/40 border border-gray-700 text-xs font-bold text-gray-200">
            Financiera Efectiva
          </span>
          <span class="px-5 py-2.5 rounded-xl bg-black/40 border border-red-500/50 text-xs font-bold text-red-400">
            Crédito Directo Grupo Lauzher
          </span>
        </div>
      </div>
    </div>
  </section>
</Layout>
''')

# --- 19. PAGES: CONCESIONARIOS ---
save('src/pages/concesionarios.astro', '''---
import Layout from '../layouts/Layout.astro';
import DealerLocator from '../components/DealerLocator.astro';
---

<Layout
  title="Concesionarios y Talleres Autorizados Nexus en Perú | Grupo Lauzher"
  description="Ubica los concesionarios oficiales y talleres mecánicos de Nexus Motos en Lima y provincias (Arequipa, Trujillo, Chiclayo, Huancayo, Tarapoto, Cusco). Sede Central en Av. Arriola."
>
  <section class="bg-gradient-to-b from-black via-[#0f121a] to-[#0b0d12] py-20 px-6 border-b border-gray-800 text-center">
    <div class="max-w-4xl mx-auto space-y-3">
      <span class="text-xs font-bold text-red-500 uppercase tracking-widest font-['Teko',sans-serif] text-base">
        PRESENCIA EN TODO EL PAÍS
      </span>
      <h1 class="text-5xl md:text-7xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight leading-none">
        PUNTOS DE VENTA Y TALLERES
      </h1>
      <p class="text-gray-300 text-base max-w-2xl mx-auto">
        Acércate a nuestro showroom principal en Av. Nicolás Arriola 2278 o a cualquiera de nuestras sedes autorizadas en el interior del Perú.
      </p>
    </div>
  </section>

  <DealerLocator />
</Layout>
''')

# --- 20. PAGES: GRUPO LAUZHER ---
save('src/pages/grupo-lauzher.astro', '''---
import Layout from '../layouts/Layout.astro';
import site from '../data/site.json';
---

<Layout
  title="Grupo Lauzher | Principal Importador Oficial de Nexus Motos en el Perú"
  description="Conoce a Grupo Lauzher: Más de 20 años importando y respaldando motocicletas y vehículos menores en el Perú. Almacén central de repuestos, garantía oficial y red nacional."
>
  <section class="bg-gradient-to-b from-black via-[#141722] to-[#0c0e14] py-20 px-6 border-b border-gray-800 text-center relative overflow-hidden">
    <div class="max-w-4xl mx-auto space-y-4 relative z-10">
      <span class="text-xs font-bold text-red-500 uppercase tracking-widest font-['Teko',sans-serif] text-base">
        MÁS DE 20 AÑOS DE TRAYECTORIA
      </span>
      <h1 class="text-5xl md:text-7xl lg:text-8xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight leading-none">
        GRUPO LAUZHER
      </h1>
      <p class="text-xl md:text-2xl font-bold uppercase text-gray-300 tracking-wider">
        EL PRINCIPAL IMPORTADOR Y REPRESENTANTE DE NEXUS EN EL PERÚ
      </p>
    </div>
  </section>

  <section class="py-20 px-6 bg-[#0c0e14] text-white">
    <div class="max-w-5xl mx-auto space-y-16">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
        <div class="space-y-4">
          <h2 class="text-3xl md:text-4xl font-black uppercase text-red-500 font-['Teko',sans-serif] tracking-wide">
            Impulsando el Progreso y la Pasión Motera
          </h2>
          <p class="text-sm text-gray-300 leading-relaxed">
            <strong>Grupo Lauzher</strong> se ha consolidado como una de las empresas importadoras más sólidas y respetadas del sector automotriz peruano. Con más de dos décadas de experiencia, nos dedicamos a la importación, ensamblaje, distribución y servicio postventa de vehículos menores de dos y tres ruedas.
          </p>
          <p class="text-sm text-gray-400 leading-relaxed">
            Como principal importador y representante de la marca <strong>Nexus</strong>, nuestro compromiso va más allá de la venta: brindamos soporte técnico especializado, capacitación continua a mecánicos y un abastecimiento ininterrumpido de repuestos originales a través de nuestro almacén logístico central en Lima.
          </p>
        </div>

        <div class="relative bg-gradient-to-br from-red-600/20 to-transparent p-1 rounded-3xl border border-gray-800">
          <div class="bg-[#12151f] rounded-3xl p-8 space-y-6">
            <div class="flex items-center gap-4">
              <span class="text-5xl font-black text-red-500 font-['Teko',sans-serif]">20+</span>
              <span class="text-xs uppercase font-bold text-gray-300">Años de Liderazgo en el Sector Motero Peruano</span>
            </div>
            <div class="flex items-center gap-4">
              <span class="text-5xl font-black text-white font-['Teko',sans-serif]">100%</span>
              <span class="text-xs uppercase font-bold text-gray-300">Garantía de Repuestos Genuinos Nexus</span>
            </div>
            <div class="flex items-center gap-4">
              <span class="text-5xl font-black text-emerald-400 font-['Teko',sans-serif]">50+</span>
              <span class="text-xs uppercase font-bold text-gray-300">Puntos de Venta y Talleres a Nivel Nacional</span>
            </div>
          </div>
        </div>
      </div>

      <div class="bg-[#121622] border border-gray-800 rounded-3xl p-8 md:p-12 space-y-6">
        <div class="text-center max-w-2xl mx-auto">
          <h3 class="text-3xl font-black uppercase text-white font-['Teko',sans-serif] tracking-wide">
            NUESTRA SEDE CENTRAL EN LIMA
          </h3>
          <p class="text-xs text-gray-400 mt-1">
            Ubicados estratégicamente en el corazón automotriz de la capital para atender a clientes y distribuidores mayoristas de todo el país.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-4 text-xs">
          <div class="bg-black/30 p-5 rounded-2xl border border-gray-800 space-y-2">
            <h4 class="font-bold text-white uppercase text-sm font-['Teko',sans-serif] text-base text-red-400">Showroom Integral</h4>
            <p class="text-gray-400">Exhibición de toda la gama Nexus 2026: pisteras, todoterreno, urbanas y trimotos con asesores comerciales expertos.</p>
          </div>
          <div class="bg-black/30 p-5 rounded-2xl border border-gray-800 space-y-2">
            <h4 class="font-bold text-white uppercase text-sm font-['Teko',sans-serif] text-base text-red-400">Taller Mecánico Especializado</h4>
            <p class="text-gray-400">Mantenimientos preventivos oficiales, diagnóstico computarizado y aplicación de garantía directa de fábrica.</p>
          </div>
          <div class="bg-black/30 p-5 rounded-2xl border border-gray-800 space-y-2">
            <h4 class="font-bold text-white uppercase text-sm font-['Teko',sans-serif] text-base text-red-400">Almacén Central de Repuestos</h4>
            <p class="text-gray-400">Despacho diario de cilindros, pistones, carburadores, kits de arrastre, plásticos y llantas a concesionarios en provincias.</p>
          </div>
        </div>

        <div class="pt-6 text-center">
          <a
            href="/contacto"
            class="inline-flex items-center gap-2 px-8 py-3.5 rounded-full text-xs font-bold uppercase tracking-wider text-white bg-red-600 hover:bg-red-700 transition-all shadow-lg"
          >
            Visitar Showroom en Av. Nicolás Arriola
          </a>
        </div>
      </div>
    </div>
  </section>
</Layout>
''')

# --- 21. PAGES: CONTACTO ---
save('src/pages/contacto.astro', '''---
import Layout from '../layouts/Layout.astro';
import site from '../data/site.json';
---

<Layout
  title="Contacto y Atención al Cliente | Nexus Motos Perú - Grupo Lauzher"
  description="Comunícate con la sede central de Grupo Lauzher en Av. Nicolás Arriola 2278, San Luis, Lima. Teléfono, WhatsApp de ventas y Libro de Reclamaciones virtual."
>
  <section class="bg-gradient-to-b from-black via-[#11151e] to-[#0c0e14] py-16 px-6 border-b border-gray-800 text-center">
    <div class="max-w-4xl mx-auto space-y-3">
      <span class="text-xs font-bold text-red-500 uppercase tracking-widest font-['Teko',sans-serif] text-base">
        CANALES OFICIALES
      </span>
      <h1 class="text-5xl md:text-7xl font-black uppercase text-white font-['Teko',sans-serif] tracking-tight leading-none">
        CONTÁCTANOS
      </h1>
      <p class="text-gray-300 text-sm md:text-base max-w-2xl mx-auto">
        Estamos listos para asesorarte en la compra de tu moto, cotización del Combo Motero o trámite de financiamiento directo.
      </p>
    </div>
  </section>

  <section class="py-16 px-6 bg-[#0c0e14] text-white">
    <div class="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12">
      <div class="lg:col-span-5 space-y-8">
        <div>
          <h2 class="text-3xl font-black uppercase text-white font-['Teko',sans-serif] tracking-wide">
            Sede Principal Grupo Lauzher
          </h2>
          <p class="text-xs text-gray-400 mt-1">
            Visítanos en nuestro showroom central de motocicletas y taller autorizado en Lima:
          </p>
        </div>

        <div class="space-y-4 text-xs">
          <div class="bg-[#141822] border border-gray-800 rounded-2xl p-5 flex items-start gap-4">
            <div class="w-10 h-10 rounded-xl bg-red-600/20 text-red-400 flex items-center justify-center flex-shrink-0">
              <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </div>
            <div>
              <span class="font-bold text-white uppercase text-sm font-['Teko',sans-serif]">Dirección Showroom</span>
              <p class="text-gray-300 font-medium mt-0.5">{site.mainAddress}</p>
              <a
                href={`https://maps.google.com/?q=${encodeURIComponent(site.mainAddress)}`}
                target="_blank"
                rel="noopener noreferrer"
                class="text-red-400 font-bold hover:underline inline-block mt-1"
              >
                Abrir en Google Maps →
              </a>
            </div>
          </div>

          <div class="bg-[#141822] border border-gray-800 rounded-2xl p-5 flex items-start gap-4">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center flex-shrink-0">
              <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
                <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.582 2.128 2.182-.573c.978.58 1.911.928 3.145.929 3.178 0 5.767-2.587 5.768-5.766.001-3.187-2.575-5.77-5.764-5.771zm3.392 8.244c-.144.405-.837.774-1.17.824-.299.045-.677.063-1.092-.069-.252-.08-.575-.187-.988-.365-1.739-.751-2.874-2.502-2.961-2.617-.087-.116-.708-.94-.708-1.793s.448-1.273.607-1.446c.159-.173.346-.217.462-.217l.332.007c.106.005.249-.04.39.298.144.347.491 1.2.534 1.287.043.087.072.188.014.303-.058.116-.087.188-.173.289l-.26.302c-.087.087-.179.182-.077.357.101.174.45 742.968 1.202.666.592 1.229.774 1.403.86.174.087.275.072.376-.044.101-.116.433-.506.549-.68.116-.173.231-.144.39-.087s1.011.477 1.184.564.289.13.332.202c.044.073.044.42-.1.825z" />
              </svg>
            </div>
            <div>
              <span class="font-bold text-white uppercase text-sm font-['Teko',sans-serif]">WhatsApp y Central Telefónica</span>
              <p class="text-gray-300 font-medium mt-0.5">Ventas: {site.centralMobile}</p>
              <p class="text-gray-300 font-medium">Central: {site.centralPhone}</p>
              <p class="text-gray-400 mt-1">{site.hours}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="lg:col-span-7 bg-[#131720] border border-gray-800 rounded-3xl p-8 shadow-2xl">
        <h3 class="text-2xl font-black uppercase text-white font-['Teko',sans-serif] tracking-wide mb-1">
          Envíanos un Mensaje
        </h3>
        <p class="text-xs text-gray-400 mb-6">Un asesor comercial se comunicará contigo a la brevedad.</p>

        <form class="space-y-4" onsubmit="event.preventDefault(); alert('¡Gracias por comunicarte con Nexus Motos Grupo Lauzher! Un asesor se pondrá en contacto contigo.');">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs uppercase font-bold text-gray-300 mb-1">Nombres y Apellidos *</label>
              <input
                type="text"
                required
                placeholder="Ej. Juan Pérez"
                class="w-full bg-[#0a0c10] border border-gray-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-red-500"
              />
            </div>
            <div>
              <label class="block text-xs uppercase font-bold text-gray-300 mb-1">Número de DNI / CE *</label>
              <input
                type="text"
                required
                placeholder="Ej. 72345678"
                class="w-full bg-[#0a0c10] border border-gray-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-red-500"
              />
            </div>
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label class="block text-xs uppercase font-bold text-gray-300 mb-1">Teléfono o Celular WhatsApp *</label>
              <input
                type="tel"
                required
                placeholder="Ej. 981234567"
                class="w-full bg-[#0a0c10] border border-gray-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-red-500"
              />
            </div>
            <div>
              <label class="block text-xs uppercase font-bold text-gray-300 mb-1">Ciudad / Departamento *</label>
              <input
                type="text"
                required
                placeholder="Ej. Lima, Arequipa, Trujillo..."
                class="w-full bg-[#0a0c10] border border-gray-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-red-500"
              />
            </div>
          </div>

          <div>
            <label class="block text-xs uppercase font-bold text-gray-300 mb-1">Modelo de Interés</label>
            <select class="w-full bg-[#0a0c10] border border-gray-700 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-red-500">
              <option>NEXUS 250R HYPER NAKED</option>
              <option>NEXUS PREDATOR 250 GP</option>
              <option>NEXUS 200 DAKAR PRO</option>
              <option>NEXUS 150 FOX URBANA</option>
              <option>NEXUS MATRIX 125 SCOOTER</option>
              <option>NEXUS TITAN 250 TRIMOTO CARGA</option>
              <option>COMBO MOTERO TODO INCLUIDO</option>
            </select>
          </div>

          <div>
            <label class="block text-xs uppercase font-bold text-gray-300 mb-1">Mensaje o Consulta</label>
            <textarea
              rows="3"
              placeholder="Deseo información sobre crédito o disponibilidad de stock..."
              class="w-full bg-[#0a0c10] border border-gray-700 rounded-xl p-3 text-xs text-white focus:outline-none focus:border-red-500"
            ></textarea>
          </div>

          <button
            type="submit"
            class="w-full py-3.5 px-6 rounded-full text-xs font-bold uppercase tracking-wider text-white bg-red-600 hover:bg-red-700 shadow-lg shadow-red-600/40 transition-all cursor-pointer"
          >
            Enviar Solicitud de Información
          </button>
        </form>
      </div>
    </div>
  </section>

  <section class="py-16 px-6 bg-[#090b0e] border-t border-gray-800" id="libro-reclamaciones">
    <div class="max-w-4xl mx-auto bg-[#13161f] border border-gray-800 rounded-3xl p-8 space-y-6">
      <div class="flex items-center gap-4">
        <div class="w-12 h-12 rounded-2xl bg-amber-500/10 text-amber-400 flex items-center justify-center">
          <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
          </svg>
        </div>
        <div>
          <h3 class="text-2xl font-black uppercase text-white font-['Teko',sans-serif]">
            Libro de Reclamaciones Virtual
          </h3>
          <p class="text-xs text-gray-400">
            Conforme a lo establecido en el Código de Protección y Defensa del Consumidor (Ley N° 29571).
          </p>
        </div>
      </div>

      <div class="text-xs text-gray-400 space-y-2 border-t border-gray-800 pt-4">
        <p><strong>Razón Social:</strong> GRUPO LAUZHER S.A.C.</p>
        <p><strong>RUC:</strong> {site.ruc}</p>
        <p><strong>Dirección:</strong> {site.mainAddress}</p>
        <p class="pt-2">
          Para presentar un reclamo o queja formal respecto a algún bien o servicio adquirido, puedes escribirnos directamente a nuestro correo de atención al consumidor: <a href={`mailto:${site.supportEmail}`} class="text-red-400 underline">{site.supportEmail}</a> o acercarte a nuestro libro físico en el showroom principal.
        </p>
      </div>
    </div>
  </section>
</Layout>
''')

print('All components and pages generated successfully!')
