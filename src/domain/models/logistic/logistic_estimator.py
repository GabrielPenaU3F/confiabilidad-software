import numpy as np


from src.domain.models.model_estimator import ModelEstimator


class LogisticEstimator(ModelEstimator):

    def calculate_mean(self, t, *model_parameters):
        a, b, c = model_parameters
        return a / (1 + self.calculate_phi(b, c, t))

    def calculate_lambda(self, t, *model_parameters):
        a, b, c = model_parameters
        phi = self.calculate_phi(b, c, t)
        numerator = a * b * phi
        denominator = (1 + phi)**2
        return numerator/denominator

    def ttf_ml_equations(self, times, vec):
        a, b, c = vec
        return (self.ttf_ml_equation_1(a, b, c, times),
                self.ttf_ml_equation_2(a, b, c, times),
                self.ttf_ml_equation_3(a, b, c, times))

    def ttf_ml_equation_1(self, a, b, c, times):
        n = len(times)
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        t_n = times[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        return n - (mu_tn - mu_t0)

    def ttf_ml_equation_2(self, a, b, c, times):
        n = len(times)
        sum_tk = np.sum(times)
        fourth_term_sum = 0
        for k in range(len(times)):
            t_k = times[k]
            psi_tk = self.calculate_psi(b, c, t_k)
            mu_tk = self.calculate_mean(t_k, a, b, c)
            fourth_term_sum += (psi_tk * mu_tk)

        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        psi_t0 = self.calculate_psi(b, c, t_0)
        t_n = times[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        psi_tn = self.calculate_psi(b, c, t_n)
        fifth_term = (mu_tn**2) * psi_tn - (mu_t0**2) * psi_t0

        return n/b + sum_tk - n * c + (2/a) * fourth_term_sum + (1/a) * fifth_term

    def ttf_ml_equation_3(self, a, b, c, times):
        n = len(times)
        second_term_sum = 0
        for k in range(len(times)):
            t_k = times[k]
            mu_tk = self.calculate_mean(t_k, a, b, c)
            phi_tk = self.calculate_phi(t_k, b, c)
            second_term_sum += mu_tk * phi_tk

        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        phi_t0 = self.calculate_phi(b, c, t_0)
        t_n = times[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        phi_tn = self.calculate_phi(b, c, t_n)
        fifth_term = (mu_tn**2) * phi_tn - (mu_t0**2) * phi_t0

        return n * a - 2 * second_term_sum - fifth_term

    def grouped_cumulative_ml_equations(self, days, cumulative_failures, vec):
        a, b, c = vec
        return (self.grouped_cumulative_ml_equation_1(a, b, c, days, cumulative_failures),
                self.grouped_cumulative_ml_equation_2(a, b, c, days, cumulative_failures),
                self.grouped_cumulative_ml_equation_3(a, b, c, days, cumulative_failures))

    def grouped_cumulative_ml_equation_1(self, a, b, c, days, cumulative_failures):
        sum = 0
        for i in range(len(days)):
            t_i = days[i]
            y_i = cumulative_failures[i]
            mu_ti = self.calculate_mean(t_i, a, b, c)
            sum += (y_i - mu_ti)

        n = len(days)
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        return sum + n * mu_t0

    def grouped_cumulative_ml_equation_2(self, a, b, c, days, cumulative_failures):
        n = len(days)
        sum = 0
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        psi_t0 = self.calculate_psi(b, c, t_0)
        for i in range(len(days)):
            y_i = cumulative_failures[i]
            t_i = days[i]
            mu_ti = self.calculate_mean(t_i, a, b, c)
            psi_ti = self.calculate_psi(b, c, t_i)
            first_term_numerator = psi_ti * (mu_ti**2) - psi_t0 * (mu_t0**2)
            first_term_denominator = psi_ti - psi_t0
            sum += (y_i * first_term_numerator/first_term_denominator - psi_ti * (mu_ti**2))
        return sum + n * psi_t0 * (mu_t0**2)

    def grouped_cumulative_ml_equation_3(self, a, b, c, days, cumulative_failures):
        n = len(days)
        sum = 0
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        phi_t0 = self.calculate_phi(b, c, t_0)
        for i in range(len(days)):
            y_i = cumulative_failures[i]
            t_i = days[i]
            mu_ti = self.calculate_mean(t_i, a, b, c)
            phi_ti = self.calculate_phi(b, c, t_i)
            first_term_numerator = phi_ti * (mu_ti**2) - phi_t0 * (mu_t0**2)
            first_term_denominator = phi_ti - phi_t0
            sum += (y_i * first_term_numerator/first_term_denominator - phi_ti * (mu_ti**2))
        return sum + n * phi_t0 * (mu_t0**2)

    def grouped_fpd_ml_equations(self, days, failures_per_day, vec):
        a, b, c = vec
        return (self.grouped_fpd_ml_equation_1(a, b, c, days, failures_per_day),
                self.grouped_fpd_ml_equation_2(a, b, c, days, failures_per_day),
                self.grouped_fpd_ml_equation_3(a, b, c, days, failures_per_day))

    def grouped_fpd_ml_equation_1(self, a, b, c, days, failures_per_day):
        deltas_yi = failures_per_day
        sum_delta_yi = np.sum(deltas_yi)
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        t_n = days[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        return sum_delta_yi - (mu_tn - mu_t0)

    def grouped_fpd_ml_equation_2(self, a, b, c, days, failures_per_day):
        deltas_yi = failures_per_day
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        psi_t0 = self.calculate_psi(b, c, t_0)
        t_n = days[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        psi_tn = self.calculate_psi(b, c, t_n)
        sum = 0
        for i in range(len(days)):
            t_i = days[i]
            if i == 0:
                t_i_minus_1 = t_0
            else:
                t_i_minus_1 = days[i - 1]
            delta_yi = deltas_yi[i]
            mu_ti = self.calculate_mean(t_i, a, b, c)
            psi_ti = self.calculate_psi(b, c, t_i)
            mu_ti_minus_1 = self.calculate_mean(t_i_minus_1, a, b, c)
            psi_ti_minus_1 = self.calculate_psi(b, c, t_i_minus_1)
            numerator = (mu_ti**2) * psi_ti - (mu_ti_minus_1**2) * psi_ti_minus_1
            denominator = mu_ti - mu_ti_minus_1
            sum += delta_yi * numerator / denominator
        return sum - ((mu_tn**2) * psi_tn - (mu_t0**2) * psi_t0)

    def grouped_fpd_ml_equation_3(self, a, b, c, days, failures_per_day):
        deltas_yi = failures_per_day
        t_0 = 0
        mu_t0 = self.calculate_mean(t_0, a, b, c)
        phi_t0 = self.calculate_phi(b, c, t_0)
        t_n = days[-1]
        mu_tn = self.calculate_mean(t_n, a, b, c)
        phi_tn = self.calculate_phi(b, c, t_n)
        sum = 0
        for i in range(len(days)):
            t_i = days[i]
            if i == 0:
                t_i_minus_1 = t_0
            else:
                t_i_minus_1 = days[i - 1]
            delta_yi = deltas_yi[i]
            mu_ti = self.calculate_mean(t_i, a, b, c)
            phi_ti = self.calculate_phi(b, c, t_i)
            mu_ti_minus_1 = self.calculate_mean(t_i_minus_1, a, b, c)
            phi_ti_minus_1 = self.calculate_phi(b, c, t_i_minus_1)
            numerator = -(mu_ti**2) * phi_ti + (mu_ti_minus_1**2) * phi_ti_minus_1
            denominator = mu_ti - mu_ti_minus_1
            sum += delta_yi * numerator / denominator
        return sum - ((mu_tn**2) * phi_tn - (mu_t0**2) * phi_t0)

    def calculate_phi(self, b, c, t):
        return np.exp(-b * (t - c))

    def calculate_psi(self, b, c, t):
        return (t - c) * self.calculate_phi(b, c, t)







