package money;

import org.junit.jupiter.api.Test;
import static org.assertj.core.api.Assertions.*;


public class DollarTest {
    @Test
    void testMultiplication() {
        Dollar five = new Dollar(5);
        assertThat(five.times(2)).isEqualTo(new Dollar(10));
        assertThat(five.times(3)).isEqualTo(new Dollar(15));
    }
}
