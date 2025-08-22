import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from astroquery.jplhorizons import Horizons

#Sol
jd={"start":"2000-01-01", "stop":"2005-01-01", "step":"1d"}
sol=Horizons(id="10", location="500@0", epochs=jd)
eph_sol=sol.vectors()

#Mercúrio
mercurio=Horizons(id="199", location = "500@0", epochs=jd)
eph_mercurio=mercurio.vectors()
x_mer=eph_mercurio["x"]
y_mer=eph_mercurio["y"]
z_mer=eph_mercurio["z"]

#Vênus
venus=Horizons(id="299", location = "500@0", epochs=jd)
eph_venus=venus.vectors()
x_ven=eph_venus["x"]
y_ven=eph_venus["y"]
z_ven=eph_venus["z"]

#Terra
terra=Horizons(id="399", location="500@0", epochs=jd)
eph_terra=terra.vectors()
x_ter=eph_terra["x"]
y_ter=eph_terra["y"]
z_ter=eph_terra["z"]

#Marte
marte= Horizons(id="499", location ="500@0", epochs=jd)
eph_marte=marte.vectors()
x_mar=eph_marte["x"]
y_mar=eph_marte["y"]
z_mar=eph_marte["z"]


#Júpiter
jupiter=Horizons(id="599", location="500@0", epochs=jd)
eph_jupiter=jupiter.vectors()
x_jup=eph_jupiter["x"]
y_jup=eph_jupiter["y"]
z_jup=eph_jupiter["z"]


#Saturno
saturno=Horizons(id="699", location="500@0", epochs=jd)
eph_saturno=saturno.vectors()
x_sat=eph_saturno["x"]
y_sat=eph_saturno["y"]
z_sat=eph_saturno["z"]


#Urano
urano=Horizons(id="799", location="500@0", epochs=jd)
eph_urano=urano.vectors()
x_ura=eph_urano["x"]
y_ura=eph_urano["y"]
z_ura=eph_urano["z"]


#Netuno
netuno=Horizons(id="899", location="500@0", epochs=jd)
eph_netuno=netuno.vectors()
x_net=eph_netuno["x"]
y_net=eph_netuno["y"]
z_net=eph_netuno["z"]


#Plutão
plutao=Horizons(id="999", location="500@0", epochs=jd)
eph_plutao=plutao.vectors()
x_plu=eph_plutao["x"]
y_plu=eph_plutao["y"]
z_plu=eph_plutao["z"]

#plotando os corpos

#Órbitas
fig=plt.figure(figsize=(12,12))
ax=fig.add_axes([0, 0, 1, 1], projection="3d")
ax.set_axis_off()
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

escala=10000
orbitas={
    
"mercurio": 0.39,
"venus": 0.72,
"terra": 1.00,
"marte": 1.52,
"jupiter": 5.20,
"saturno": 9.58,
"urano": 19.18,
"netuno": 30.07,
"plutão": 39.48
}
theta=np.linspace(0, 2*np.pi, 200)
fator_espaco=2


# Gerando coordenadas circulares para cada corpo (em vez de usar os dados do JPL)
theta = np.linspace(0, 2*np.pi, 200)

x_mer = orbitas["mercurio"] * np.cos(theta) * fator_espaco
y_mer = orbitas["mercurio"] * np.sin(theta) * fator_espaco
z_mer = np.zeros_like(theta)

x_ven = orbitas["venus"] * np.cos(theta) * fator_espaco
y_ven = orbitas["venus"] * np.sin(theta) * fator_espaco
z_ven = np.zeros_like(theta)

x_ter = orbitas["terra"] * np.cos(theta) * fator_espaco
y_ter = orbitas["terra"] * np.sin(theta) * fator_espaco
z_ter = np.zeros_like(theta)

x_mar = orbitas["marte"] * np.cos(theta) * fator_espaco
y_mar = orbitas["marte"] * np.sin(theta) * fator_espaco
z_mar = np.zeros_like(theta)

x_jup = orbitas["jupiter"] * np.cos(theta) * fator_espaco
y_jup = orbitas["jupiter"] * np.sin(theta) * fator_espaco
z_jup = np.zeros_like(theta)

x_sat = orbitas["saturno"] * np.cos(theta) * fator_espaco
y_sat = orbitas["saturno"] * np.sin(theta) * fator_espaco
z_sat = np.zeros_like(theta)

x_ura = orbitas["urano"] * np.cos(theta) * fator_espaco
y_ura = orbitas["urano"] * np.sin(theta) * fator_espaco
z_ura = np.zeros_like(theta)

x_net = orbitas["netuno"] * np.cos(theta) * fator_espaco
y_net = orbitas["netuno"] * np.sin(theta) * fator_espaco
z_net = np.zeros_like(theta)

x_plu = orbitas["plutão"] * np.cos(theta) * fator_espaco
y_plu = orbitas["plutão"] * np.sin(theta) * fator_espaco
z_plu = np.zeros_like(theta)

for corpo, raio in orbitas.items():
    x=raio*np.cos(theta)*fator_espaco
    y=raio*np.sin(theta)*fator_espaco
    z=np.zeros_like(theta)

    ax.plot(x, y, z, label=corpo)


#Sol

ax.scatter(0, 0, 0, color="yellow", s=200, label="sol")

# Anel de Saturno
r_in_sat = 6
r_out_sat = 3
theta_ring = np.linspace(0, 2*np.pi, 100)
x_ring_sat = (r_in_sat + (r_out_sat-r_in_sat)/2) * np.cos(theta_ring) + x_sat[0]
y_ring_sat = (r_in_sat + (r_out_sat-r_in_sat)/2) * np.sin(theta_ring) + y_sat[0]
z_ring_sat = np.zeros_like(theta_ring) + z_sat[0]
ring_sat, = ax.plot(x_ring_sat, y_ring_sat, z_ring_sat, color="gold", alpha=0.6, linewidth=2)

#Urano
# Anel de Urano 
r_in_ura = 4
r_out_ura = 2
R_ura = (r_in_ura + (r_out_ura - r_in_ura)/2)
phi = np.deg2rad(98)

x_ring_ura = R_ura * np.cos(theta_ring)
y_ring_ura = R_ura * np.sin(theta_ring)
z_ring_ura = np.zeros_like(theta_ring)

y_rot = y_ring_ura * np.cos(phi) - z_ring_ura * np.sin(phi)
z_rot = y_ring_ura * np.sin(phi) + z_ring_ura * np.cos(phi)

x_ring_ura = x_ring_ura + x_ura[0]
y_ring_ura = y_rot + y_ura[0]
z_ring_ura = z_rot + z_ura[0]

ring_ura, = ax.plot(x_ring_ura, y_ring_ura, z_ring_ura, color="lightblue", alpha=0.5, linewidth=1)

#Fundo preto
ax.set_facecolor("black")

#Estrelas aleatórias
num_estrelas=1000
xs=np.random.uniform(-335, 335, num_estrelas)
ys=np.random.uniform(-35, 35, num_estrelas)
zs=np.random.uniform(-35, 35, num_estrelas)
ax.scatter(xs, ys, zs, color="white", s=2)

theta=np.linspace(0, 2*np.pi, 200)



limite=45
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.set_zlim(-5, 5)
ax.set_xlabel("X (UA)")
ax.set_ylabel("Y (UA)")
ax.set_zlabel("Z (UA)")
ax.legend()

#Animando 
corpo_mer=ax.scatter(x_mer[0], y_mer[0], z_mer[0], color="gray", s=37)
corpo_ven=ax.scatter(x_ven[0], y_ven[0], z_ven[0], color="orange", s=58)
corpo_ter=ax.scatter(x_ter[0], y_ter[0], z_ter[0], color="green", s=60)
corpo_mar=ax.scatter(x_mar[0], y_mar[0], z_mar[0], color="red", s=44)
corpo_jup=ax.scatter(x_jup[0], y_jup[0], z_jup[0], color="beige", s=199)
corpo_sat=ax.scatter(x_sat[0], y_sat[0], z_sat[0], color="gold", s=181)
corpo_ura=ax.scatter(x_ura[0], y_ura[0], z_ura[0], color="lightblue", s=120)
corpo_net=ax.scatter(x_net[0], y_net[0], z_net[0], color="darkblue", s=118)
corpo_plu=ax.scatter(x_plu[0], y_plu[0], z_plu[0], color="white", s=26)

periodos = {
    "mercurio": 0.24,  # 88 dias
    "venus": 0.62,     # 225 dias
    "terra": 1.00,     # 365 dias
    "marte": 1.88,     # 687 dias
    "jupiter": 11.86,
    "saturno": 29.45,
    "urano": 84.0,
    "netuno": 164.8,
    "plutao": 248.0
}
# Deslocamentos iniciais
offset_mer = 20
offset_ven = 50
offset_ter = 100
offset_mar = 150
offset_jup = 10
offset_sat = 30
offset_ura = 70
offset_net = 120
offset_plu = 5

# Fatores de velocidade (quanto cada planeta anda por frame)
vel_mer = 4      # Mercúrio rápido
vel_ven = 2
vel_ter = 1
vel_mar = 0.53
vel_jup = 0.08
vel_sat = 0.034
vel_ura = 0.012
vel_net = 0.006
vel_plu = 0.004

def update(i):
    # Mercúrio
    idx = int(i*vel_mer + offset_mer) % len(x_mer)
    corpo_mer._offsets3d = ([x_mer[idx]], [y_mer[idx]], [z_mer[idx]])

    # Vênus
    idx = int(i*vel_ven + offset_ven) % len(x_ven)
    corpo_ven._offsets3d = ([x_ven[idx]], [y_ven[idx]], [z_ven[idx]])

    # Terra
    idx = int(i*vel_ter + offset_ter) % len(x_ter)
    corpo_ter._offsets3d = ([x_ter[idx]], [y_ter[idx]], [z_ter[idx]])

    # Marte
    idx = int(i*vel_mar + offset_mar) % len(x_mar)
    corpo_mar._offsets3d = ([x_mar[idx]], [y_mar[idx]], [z_mar[idx]])

    # Júpiter
    idx = int(i*vel_jup + offset_jup) % len(x_jup)
    corpo_jup._offsets3d = ([x_jup[idx]], [y_jup[idx]], [z_jup[idx]])

    # Saturno
    idx = int(i*vel_sat + offset_sat) % len(x_sat)
    corpo_sat._offsets3d = ([x_sat[idx]], [y_sat[idx]], [z_sat[idx]])

    # Atualizar anel de Saturno (permanece plano)
    x_ring_sat = (r_in_sat + (r_out_sat-r_in_sat)/2) * np.cos(theta_ring) + x_sat[idx]
    y_ring_sat = (r_in_sat + (r_out_sat-r_in_sat)/2) * np.sin(theta_ring) + y_sat[idx]
    z_ring_sat = np.zeros_like(theta_ring) + z_sat[idx]
    ring_sat.set_data(x_ring_sat, y_ring_sat)
    ring_sat.set_3d_properties(z_ring_sat)

    # Urano
    idx = int(i*vel_ura + offset_ura) % len(x_ura)
    corpo_ura._offsets3d = ([x_ura[idx]], [y_ura[idx]], [z_ura[idx]])

    #anel de Urano inclinado
    R_ura = (r_out_ura - r_in_ura)/2
    R_med=(r_out_ura + r_in_ura)/2
    phi = np.deg2rad(98)  
    x_ring_ura = R_ura * np.cos(theta_ring)
    y_ring_ura = R_ura * np.sin(theta_ring)
    z_ring_ura = np.zeros_like(theta_ring)

    y_rot = y_ring_ura * np.cos(phi) - z_ring_ura * np.sin(phi)
    z_rot = y_ring_ura * np.sin(phi) + z_ring_ura * np.cos(phi)

    x_ring_ura = x_ring_ura + x_ura[idx]
    y_ring_ura = y_rot + y_ura[idx]
    z_ring_ura = z_rot + z_ura[idx]

    ring_ura.set_data(x_ring_ura, y_ring_ura)
    ring_ura.set_3d_properties(z_ring_ura)

    # Netuno
    idx = int(i*vel_net + offset_net) % len(x_net)
    corpo_net._offsets3d = ([x_net[idx]], [y_net[idx]], [z_net[idx]])

    # Plutão
    idx = int(i*vel_plu + offset_plu) % len(x_plu)
    corpo_plu._offsets3d = ([x_plu[idx]], [y_plu[idx]], [z_plu[idx]])

    return (corpo_mer, corpo_ven, corpo_ter, corpo_mar, corpo_jup, corpo_sat, corpo_ura, corpo_net, corpo_plu, ring_sat, ring_ura)

ani=FuncAnimation(fig, update, interval=50, blit=False)
plt.show()