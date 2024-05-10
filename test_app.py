import unittest
import json
from app import app

class TestApp(unittest.TestCase):
    def test_create_order(self):
        # Test valid order
        client = app.test_client()
        payload = {
            "components": ["I", "A", "D", "F", "K"]
        }
        response = client.post('/orders', json=payload)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertTrue('order_id' in data)
        self.assertAlmostEqual(data['total'], 142.3, places=2)
        self.assertListEqual(data['parts'], ["Android OS", "LED Screen", "Wide-Angle Camera", "USB-C Port", "Metallic Body"])
    
    def test_duplicate_component_type(self):
        # Test order with duplicate component type
        client = app.test_client()
        payload = {
            "components": ["I", "A", "D", "F", "F"]
        }
        response = client.post('/orders', json=payload)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertTrue('error' in data)
        self.assertEqual(data['error'], "Duplicate component type: Port")

    def test_missing_component_types(self):
        # Test order with missing component types
        client = app.test_client()
        payload = {
            "components": ["I", "A", "D"]
        }
        response = client.post('/orders', json=payload)
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertTrue('error' in data)
        self.assertEqual(data['error'], "Missing component types")

if __name__ == '__main__':
    unittest.main()
