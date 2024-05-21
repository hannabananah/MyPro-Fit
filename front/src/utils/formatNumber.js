export function formatNumberWithCommas(number) {
  if (!number) return '';
  const parts = number.toString().split('.');
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  return parts.join('.');
}

export function parseNumberWithCommas(string) {
  if (!string && string !== 0) return 0;
  return parseFloat(string.toString().replace(/,/g, ''));
}
