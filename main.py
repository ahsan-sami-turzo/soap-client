import http.client
from xml.etree import ElementTree as ET


def send_soap_request():
    # Create HTTP connection
    conn = http.client.HTTPConnection('localhost', 8081)

    # Define SOAP request body
    soap_request = """
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <getFinlandCities/>
        </soap:Body>
    </soap:Envelope>
    """

    # Send HTTP request
    headers = {'Content-Type': 'text/xml', 'SOAPAction': '#POST'}
    conn.request('POST', '/', soap_request, headers)

    # Get HTTP response
    response = conn.getresponse()

    # Decode the response body and parse SOAP response
    soap_response = ET.fromstring(response.read().decode())
    # print(soap_response)
    # Print all city names and expenses
    for city in soap_response.findall('.//{http://www.example.com/your-namespace}city'):
        name = city.find('{http://www.example.com/your-namespace}name').text
        expense = city.find('{http://www.example.com/your-namespace}expense').text
        print(f'City: {name}, Expense: {expense}')

    # Close HTTP connection
    conn.close()


if __name__ == '__main__':
    send_soap_request()
