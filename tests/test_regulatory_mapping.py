from governance.regulatory_mapping import regulatory_mapping_table


def test_regulatory_mapping_contains_backtesting():
    table = regulatory_mapping_table()
    assert '250-business-day VaR backtesting' in set(table['requirement_or_concept'])
