package money;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;


public class FrancTest {
    @Test
    void testMultiplication() {
        Franc five = new Franc(5);
        assertThat(five.times(2)).isEqualTo(new Franc(10));
        assertThat(five.times(3)).isEqualTo(new Franc(15));
    }

    @Test
    void testEquality() {
        assertThat(new Franc(5)).isEqualTo(new Franc(5));
        assertThat(new Franc(5)).isNotEqualTo(new Franc(6));
    }
}
