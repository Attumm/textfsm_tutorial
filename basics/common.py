import textfsm
from io import StringIO


def run_textfsm(output, template):
    """Parses text output using a TextFSM template and returns structured data.

    This function takes raw text output and a TextFSM template as input.
    It uses the TextFSM library to parse the output according to the provided
    template. The parsed data is then structured into a list of dictionaries,
    where each dictionary represents a record extracted from the output.
    The keys of each dictionary are derived from the header defined in the
    TextFSM template.

    Args:
        output (str): The raw text output to be parsed. This is typically
            the output from a command-line interface or a log file.
        template (str): The TextFSM template string. This template defines
            the patterns and header to be used for parsing the `output` text.

    Returns:
        list[dict]: A list of dictionaries. Each dictionary represents a
            record parsed from the `output`. The keys of the
            dictionaries are the headers defined in the TextFSM
            template, and the values are the corresponding parsed
            data for each record. Returns an empty list if no records
            are parsed.

    Examples:
        >>> output_text = '''
        ... Device Name                   IP Address     State
        ... -------------               ----------     -----
        ... RouterA                       192.168.1.1    Up
        ... SwitchB                       10.0.0.1       Down
        ... '''
        >>> template_text = '''
        ... Value Device (.+)
        ... Value IPAddress (\\\\d+\\\\.\\\\d+\\\\.\\\\d+\\\\.\\\\d+)
        ... Value State (Up|Down)
        ...
        ... Start
        ... ^${Device}\\\\s+ ${IPAddress}\\\\s+ ${State} -> Record
        ... '''
        >>> result = run_textfsm(output_text, template_text)
        >>> print(result)
        [{'Device': 'RouterA', 'IPAddress': '192.168.1.1', 'State': 'Up'}, {'Device': 'SwitchB', 'IPAddress': '10.0.0.1', 'State': 'Down'}]
    """
    t = textfsm.TextFSM(StringIO(template))
    raw_list = t.ParseText(output.strip())
    return [dict(zip(t.header, i)) for i in raw_list]
