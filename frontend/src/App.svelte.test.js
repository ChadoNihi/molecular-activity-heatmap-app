import { render } from '@testing-library/svelte';
import App from './App.svelte';

test('should be rendered', () => {
  expect(render(App)).toBe(true);
});
