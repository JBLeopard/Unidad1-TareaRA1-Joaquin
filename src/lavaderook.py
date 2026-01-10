# lavadero.py
"""
Módulo lavadero.py

Este módulo contiene la clase Lavadero, que simula el funcionamiento
de un lavadero de coches automático con distintas opciones:
- prelavado a mano
- secado a mano
- encerado

El lavadero avanza por diferentes fases según las opciones seleccionadas
y acumula ingresos en función del tipo de lavado realizado.
"""
class Lavadero:
    """
    Clase que representa un lavadero de coches.

    Gestiona:
    - El estado del lavadero (ocupado / inactivo)
    - Las fases del proceso de lavado
    - Los ingresos acumulados
    - Las reglas de negocio definidas en el enunciado
    """
 # Constantes que representan las distintas fases del lavadero
    FASE_INACTIVO = 0               # Lavadero parado, sin coches 
    FASE_COBRANDO = 1               # Cobro del lavado
    FASE_PRELAVADO_MANO = 2         # Prelavado manual 
    FASE_ECHANDO_AGUA = 3           # Aclarado con agua
    FASE_ENJABONANDO = 4            # Aplicación de jabón
    FASE_RODILLOS = 5               # Limpieza con rodillos
    FASE_SECADO_AUTOMATICO = 6      # Secado automático
    FASE_SECADO_MANO = 7            # Secado manual
    FASE_ENCERADO = 8               # Encerado manual

    def __init__(self):
        """
        Constructor del lavadero.
        Inicializa el lavadero cumpliendo el requisito:
        - ingresos a 0
        - no ocupado
        - fase inactiva (0)
        - todas las opciones de lavado desactivadas
        """
        self.__ingresos = 0.0
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
        self.terminar() 

    @property
    def fase(self):
        return self.__fase

    @property
    def ingresos(self):
        return self.__ingresos

    @property
    def ocupado(self):
        return self.__ocupado
    
    @property
    def prelavado_a_mano(self):
        return self.__prelavado_a_mano

    @property
    def secado_a_mano(self):
        return self.__secado_a_mano

    @property
    def encerado(self):
        return self.__encerado

    def terminar(self):
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
    
    def hacerLavado(self, prelavado_a_mano, secado_a_mano, encerado):
        """
        Inicia un nuevo lavado estableciendo las opciones seleccionadas.
        
        Reglas de negocio:
        - No se puede iniciar un lavado si el lavadero está ocupado
        - No se permite el encerado sin secado a mano

        :raises RuntimeError: Si el lavadero está ocupado
        :raises ValueError: Si se intenta encerar sin secado a mano
        """
        if self.__ocupado:
            raise RuntimeError("No se puede iniciar un nuevo lavado mientras el lavadero está ocupado")
        
        if not secado_a_mano and encerado:
            raise ValueError("No se puede encerar el coche sin secado a mano")
        
        self.__fase = self.FASE_INACTIVO  
        self.__ocupado = True
        self.__prelavado_a_mano = prelavado_a_mano
        self.__secado_a_mano = secado_a_mano
        self.__encerado = encerado
        

    def _cobrar(self):
        """
        Calcula el precio del lavado según las opciones seleccionadas.
     
        Precio base: 5.00 €
        Incrementos modificados para pasar los tests unitarios:
        - Prelavado a mano: +1.50 €
        - Secado a mano: +1.00 €   <-- CAMBIO: antes 1.20, ahora coincide con test5
        - Encerado: +1.20 €        <-- CAMBIO: antes 1.00, ahora coincide con test6
        """
        coste_lavado = 5.00
        
        if self.__prelavado_a_mano:
            coste_lavado += 1.50 
        
        if self.__secado_a_mano:
            coste_lavado += 1.00  # Cambio para pasar test5
        
        if self.__encerado:
            coste_lavado += 1.20  # Cambio para pasar test6
        
        self.__ingresos += coste_lavado
        return coste_lavado

    def avanzarFase(self):
        """
        Avanza el lavadero a la siguiente fase del proceso.
        """
        if not self.__ocupado:
            return

        if self.__fase == self.FASE_INACTIVO:
            coste_cobrado = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f" (COBRADO: {coste_cobrado:.2f} €) ", end="")
        elif self.__fase == self.FASE_COBRANDO:
            if self.__prelavado_a_mano:
                self.__fase = self.FASE_PRELAVADO_MANO
            else:
                self.__fase = self.FASE_ECHANDO_AGUA 
        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA
        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO
        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS
        elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_MANO  # CAMBIO: corregido flujo secado
            else:
                self.__fase = self.FASE_SECADO_AUTOMATICO
        elif self.__fase == self.FASE_SECADO_AUTOMATICO:
            self.terminar()
        elif self.__fase == self.FASE_SECADO_MANO:
            if self.__encerado:
                self.__fase = self.FASE_ENCERADO  # CAMBIO: flujo correcto para test12/test14
            else:
                self.terminar()
        elif self.__fase == self.FASE_ENCERADO:
            self.terminar()
        else:
            raise RuntimeError(f"Estado no válido: Fase {self.__fase}. El lavadero va a estallar...")


    def imprimir_fase(self):
        fases_map = {
            self.FASE_INACTIVO: "0 - Inactivo",
            self.FASE_COBRANDO: "1 - Cobrando",
            self.FASE_PRELAVADO_MANO: "2 - Haciendo prelavado a mano",
            self.FASE_ECHANDO_AGUA: "3 - Echándole agua",
            self.FASE_ENJABONANDO: "4 - Enjabonando",
            self.FASE_RODILLOS: "5 - Pasando rodillos",
            self.FASE_SECADO_AUTOMATICO: "6 - Haciendo secado automático",
            self.FASE_SECADO_MANO: "7 - Haciendo secado a mano",
            self.FASE_ENCERADO: "8 - Encerando a mano",
        }
        print(fases_map.get(self.__fase, f"{self.__fase} - En estado no válido"), end="")


    def imprimir_estado(self):
        print("----------------------------------------")
        print(f"Ingresos Acumulados: {self.ingresos:.2f} €")
        print(f"Ocupado: {self.ocupado}")
        print(f"Prelavado a mano: {self.prelavado_a_mano}")
        print(f"Secado a mano: {self.secado_a_mano}")
        print(f"Encerado: {self.encerado}")
        print("Fase: ", end="")
        self.imprimir_fase()
        print("\n----------------------------------------")
        

    # FUNCIONES AUXILIARES PARA TESTS
    def ejecutar_y_obtener_fases(self, prelavado, secado, encerado):
        """
        Método auxiliar utilizado exclusivamente para pruebas unitarias.

        Ejecuta un ciclo completo de lavado y devuelve una lista con
        todas las fases por las que ha pasado el lavadero.
        """
        self.hacerLavado(prelavado, secado, encerado)  # CAMBIO: corregido _hacer_lavado → hacerLavado
        fases_visitadas = [self.fase]

        while self.ocupado:
            # Usamos un límite de pasos para evitar bucles infinitos
            if len(fases_visitadas) > 15:
                raise Exception("Bucle infinito detectado en la simulación de fases.")
            self.avanzarFase()
            fases_visitadas.append(self.fase)

        return fases_visitadas
