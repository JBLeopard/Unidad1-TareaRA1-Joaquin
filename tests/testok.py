import unittest
from lavadero import Lavadero


class TestLavadero(unittest.TestCase):

    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

    # ---------------------------------------------------------
    # TEST 1
    # ---------------------------------------------------------
    def test1_estado_inicial_inactivo(self):
        """Test 1: Estado inicial del lavadero."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)

    # ---------------------------------------------------------
    # TEST 2
    # ---------------------------------------------------------
    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Encerado sin secado a mano lanza ValueError."""
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(False, False, True)

    # ---------------------------------------------------------
    # TEST 3
    # ---------------------------------------------------------
    def test3_excepcion_lavadero_ocupado(self):
        """Test 3: No se puede iniciar un lavado si ya está ocupado."""
        self.lavadero.hacerLavado(False, False, False)
        with self.assertRaises(RuntimeError):
            self.lavadero.hacerLavado(False, False, False)

    # ---------------------------------------------------------
    # TESTS DE INGRESOS
    # ---------------------------------------------------------
    def test4_ingresos_prelavado(self):
        """Test 4: Prelavado a mano = 6.50 €"""
        self.lavadero.hacerLavado(True, False, False)
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.ingresos, 6.50)

    def test5_ingresos_secado_mano(self):
        """Test 5: Secado a mano = 6.00 €"""
        self.lavadero.hacerLavado(False, True, False)
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.ingresos, 6.00)

    def test6_ingresos_secado_y_encerado(self):
        """Test 6: Secado a mano + encerado = 7.20 €"""
        self.lavadero.hacerLavado(False, True, True)
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.ingresos, 7.20)

    def test7_ingresos_prelavado_y_secado(self):
        """Test 7: Prelavado + secado a mano = 7.50 €"""
        self.lavadero.hacerLavado(True, True, False)
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.ingresos, 7.50)

    def test8_ingresos_completo(self):
        """Test 8: Prelavado + secado a mano + encerado = 8.70 €"""
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero.avanzarFase()
        self.assertEqual(self.lavadero.ingresos, 8.70)

    # ---------------------------------------------------------
    # TESTS DE FLUJO DE FASES
    # ---------------------------------------------------------
    def test9_flujo_sin_extras(self):
        """Test 9: Flujo sin extras."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
        fases = self.lavadero.ejecutar_y_obtener_fases(False, False, False)
        self.assertEqual(fases, fases_esperadas)

    def test10_flujo_prelavado(self):
        """Test 10: Flujo con prelavado."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]
        fases = self.lavadero.ejecutar_y_obtener_fases(True, False, False)
        self.assertEqual(fases, fases_esperadas)

    def test11_flujo_secado_mano(self):
        """Test 11: Flujo con secado a mano."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]
        fases = self.lavadero.ejecutar_y_obtener_fases(False, True, False)
        self.assertEqual(fases, fases_esperadas)

    def test12_flujo_secado_y_encerado(self):
        """Test 12: Flujo con secado a mano y encerado."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 8, 0]
        fases = self.lavadero.ejecutar_y_obtener_fases(False, True, True)
        self.assertEqual(fases, fases_esperadas)

    def test13_flujo_prelavado_y_secado(self):
        """Test 13: Flujo con prelavado y secado a mano."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]
        fases = self.lavadero.ejecutar_y_obtener_fases(True, True, False)
        self.assertEqual(fases, fases_esperadas)

    def test14_flujo_completo(self):
        """Test 14: Flujo completo."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        fases = self.lavadero.ejecutar_y_obtener_fases(True, True, True)
        self.assertEqual(fases, fases_esperadas)


if __name__ == "__main__":
    unittest.main()
